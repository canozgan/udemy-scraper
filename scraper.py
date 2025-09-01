import time
from camoufox.sync_api import Camoufox
from bs4 import BeautifulSoup
import csv
import os
import random


class Scraper():

    def get_page_html(url, retries=3, delay=5):
        '''
        Open the given URL with Camoufox and return the page HTML.
        Includes retry logic in case of errors or slow loading.
        '''
        attempt = 0

        while attempt < retries:
            attempt += 1
            print(f"\n[INFO] Attempt {attempt}/{retries} for {url}")

            camoufox_args = {
                "headless": True,
                "humanize": True,
                "window": (1280, 720)
            }

            try:
                with Camoufox(**camoufox_args) as browser:
                    page = browser.new_page()
                    page.goto(url)

                    # Wait until page is stable
                    page.wait_for_load_state(state="domcontentloaded")
                    page.wait_for_load_state("networkidle")

                    rand = 5000 + random.randint(1000, 5000)
                    page.wait_for_timeout(rand)  # wait 5+ seconds

                    page.locator(
                        "section.vertical-card-module--card--Lgh-9"
                    ).first.wait_for(timeout=5000)

                    html = page.content()
                    return html  # success

            except Exception as e:
                print(f"[ERROR] Attempt {attempt} failed: {e}")

            if attempt < retries:
                random_delay = delay + random.randint(1, 5)
                print(f"[INFO] Retrying in {random_delay} seconds...")
                time.sleep(random_delay)

        print("[FATAL] All retry attempts failed.")
        return None

    def parse_items(html, item_counter):
        """
        Parse items from the given HTML using BeautifulSoup.
        """
        soup = BeautifulSoup(html, "html.parser")
        items = soup.select("section.vertical-card-module--card--Lgh-9")

        # Name of the CSV file
        csv_file = "results.csv"

        # If the file does not exist, create it and write the header row
        if not os.path.exists(csv_file):
            with open(csv_file, mode="w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["Item", "Title", "Rating", "Price"])

        for item in items:
            item_counter += 1

            # Extract title
            title = item.select_one(
                "div.card-title-module--clipped--DPJnT"
            )
            title_text = title.get_text(strip=True) if title else "N/A"

            # Extract rating
            rating = item.select_one(
                "span.star-rating-module--star-wrapper--i1cJH "
                "span.star-rating-module--rating-number--2-qA2"
            )
            rating_text = rating.get_text(strip=True) if rating else "N/A"

            # Extract price
            price = item.select_one(
                "div.base-price-text-module--price-part---xQlz span span"
            )
            price_text = price.get_text(strip=True) if price else "N/A"

            # Print results
            print(f"\nItem {item_counter}")
            print("Title:", title_text)
            print("Rating:", rating_text)
            print("Price:", price_text)

            # Append the current item to the CSV file
            with open(csv_file, mode="a", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow([
                    item_counter,
                    title_text,
                    rating_text,
                    price_text
                ])

        return item_counter

    def scrape_page(url, item_counter):
        """
        High-level function to scrape one page.
        """
        html = Scraper.get_page_html(url)
        if html:
            item_counter = Scraper.parse_items(html, item_counter)
        else:
            print("[ERROR] Could not scrape page after retries.")

        return item_counter
