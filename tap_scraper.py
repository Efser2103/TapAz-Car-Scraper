from playwright.sync_api import sync_playwright
import pandas as pd
from time import sleep, time

baslangic=time()
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://tap.az/elanlar/neqliyyat/avtomobiller?keywords_source=typewritten&p%5B745%5D=3802")
    cars = []
    car_set=set()
    while True:
        announcements = page.locator("a[class='AdCardNew-styled__Card-sc-5e8cdaf0-15 cBYzRd']")
        announcement_count= announcements.count()
        for i in range(announcement_count):
            announcement = announcements.nth(i)
            announcement_link =  "https://tap.az"+announcement.get_attribute("href") 
            if announcement_link in car_set:
                continue
            car_set.add(announcement_link)
            link= f'=HYPERLINK("{announcement_link}", "Linke kec")'
            name_year=announcement.locator("p[data-testid='ad-card-title']").inner_text()          
            price=announcement.locator("p[data-testid='ad-card-price']").inner_text()
            cars.append({"Name and Year": name_year, "Price": price, "Announcement Link": link})
        last_height = page.evaluate("document.body.scrollHeight")
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        page.wait_for_timeout(2000)
        new_height = page.evaluate("document.body.scrollHeight")
        if new_height == last_height:
            break
df = pd.DataFrame(cars, columns=["Name and Year", "Price", "Announcement Link"])
excel_fayli = "tap_masinlar.xlsx"        
df.to_excel(excel_fayli, index=False)
son=time()
print(f"FINISHED! {son-baslangic} seconds")