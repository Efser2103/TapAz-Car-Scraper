# Tap.az Car Listings Web Scraper

A Python automation script built using **Playwright** and **Pandas** to extract live car listing data from Tap.az and export it into a clean, formatted Excel spreadsheet.

## Features

- **Dynamic Data Extraction:** Extracts car titles, prices, and generated Excel hyperlinks (`=HYPERLINK`).
- **Clean Data Formatting:** Exports directly to `.xlsx` using Pandas.
- **Duplicate Prevention:** Uses Python `sets` to prevent duplicate listings during scraping.

## How to Run

```bash
git clone [https://github.com/Efser2103/TapAz-Car-Scraper.git](https://github.com/Efser2103/TapAz-Car-Scraper.git)
pip install playwright pandas openpyxl
python -m playwright install chromium
python tap_scraper.py
