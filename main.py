from scraper import Scraper
import sys

def main(page_number, searched_course):
    print(f"Scraping courses: {searched_course}")
    print(f"Scraping total pages: {page_number}")

    
    item_counter = 0
    page_counter = 0

    for page_counter in range(1,page_number+1):

        url = (
            f"https://www.udemy.com/courses/search/"
            f"?p={page_counter}"
            f"&q={searched_course}&src=ukw"
        )
    
        item_counter = Scraper.scrape_page(url, item_counter)

    print(f"\n\nTotal items found: {item_counter}")
    print(f"Total pages crawled: {page_number}")
    print("All items were saved to the results.csv file")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python main.py <page_number> <searched_course>")
    else:
        try:
            page_number = int(sys.argv[1])
            searched_course = sys.argv[2]

            if page_number < 1:
                print("Error: item_number must be greater than 0")
            else:
                main(page_number, searched_course)
        except ValueError:
            print("Error: page_number must be an integer")

    

