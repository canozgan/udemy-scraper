# Udemy Scraper 🚀

This project uses an AI-powered **headless browser** to mimic human interactions, bypass **Cloudflare protections**, and scrape course information from Udemy. The results are exported in CSV format for further analysis.

---

## 📦 Installation

Clone the repository:
```bash
git clone https://github.com/canozgan/udemy-scraper.git
cd udemy-scraper
```

Create a virtual environment and install dependencies:
```bash
python3 -m venv venv
source venv/bin/activate   # Linux / macOS
# or
.\venv\Scripts\activate    # Windows PowerShell

pip install -r requirements.txt
```

---

## ▶️ Usage

Run the scraper with:
```bash
python main.py <page_number> <searched_course>
```

**page_number** → the number of the search results page you want to scrape

**searched_course** → the keyword to search for courses (e.g., python, javascript)

Example:

```bash
python main.py 1 python
```

Results will be saved into results.csv.
An example output file is included: example_results.csv.

---

## 📂 Project Structure

```
udemy-scraper/
├── main.py
├── scraper.py
├── requirements.txt
├── results.csv        # generated after running the scraper
├── example_results.csv
└── README.md
```

---

## 🛠️ Technologies & Libraries

**[Camoufox](https://pypi.org/project/camoufox/)** – Headless browser that mimics human-like behavior

**[BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)** – HTML parsing

**Python standard libraries**: csv, os, time, random

---

## ⚠️ Disclaimer

This project is intended for educational purposes only.
You are solely responsible for how you use it.
Please do not use it in ways that violate [Udemy’s Terms of Service](https://www.udemy.com/terms/).







