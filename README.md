# Amazon Product Data Scraper & Sentiment Analyzer



This repository provides Python scripts for scraping product data and reviews from Amazon, exporting them to CSV, and performing sentiment analysis on the collected reviews. The project demonstrates both Selenium-based and requests-based scraping approaches, and leverages BeautifulSoup, pandas, and TextBlob for parsing, data handling, and sentiment analysis.

Features
Product Data Scraping:
Extract product title, price (MRP and ASP), and rating from Amazon search result pages.

Review Scraping:
Collects recent reviews for a given Amazon product, including review text and review date.

Sentiment Analysis:
Analyzes review sentiment (positive, negative, neutral) with confidence scores using TextBlob.

CSV Export:
Saves collected product and review data to CSV for further analysis.

Customizable & Extensible:
Easily adapt the scripts for different Amazon domains or product categories.

Project Structure

text
.
├── amazon_selenium.py              # Selenium-based product data scraper

├── amazonscrapper-csvofthedata.py # Requests-based review scraper & sentiment analyzer

├── amazon_laptops.csv              # Example output: scraped product data

├── dsduscu.csv                     # Example output: scraped reviews & sentiment

└── README.md                       # You are here!

 Requirements
Python 3.7+

Google Chrome (for Selenium)

ChromeDriver (for Selenium)

pip packages:
selenium, beautifulsoup4, pandas, requests, textblob

Install dependencies:

bash
pip install selenium beautifulsoup4 pandas requests textblob
 Usage
1. Scrape Product Data (Selenium)
Edit amazon_selenium.py and set your search query (default: "laptop").

Run the script:

bash
python amazon_selenium.py
Output: amazon_laptops.csv with columns: Title, MRP, ASP, Rating.

2. Scrape Reviews & Analyze Sentiment
Run amazonscrapper-csvofthedata.py.

Enter the product code (ASIN) when prompted (e.g., B0C4YRBB8Z).

The script collects recent reviews, analyzes sentiment, and saves results to dsduscu.csv.

 Example Output
amazon_laptops.csv

Title	MRP	ASP	Rating

HP 15s, 12th Gen i3 ...	₹45,999	₹39,990	4.2 out of 5 stars

...	...	...	...

dsduscu.csv

Review	Date	sentiment	confidence
Great laptop for students!	2024-06-20	positive	0.65
Battery life is disappointing.	2024-06-19	negative	0.50

...	...	...	...

How It Works

Product Scraping (amazon_selenium.py)
Uses Selenium to load Amazon search results.

Parses product cards with BeautifulSoup.

Extracts title, price, and rating for each product.



Saves results to CSV.

Review Scraping & Sentiment (amazonscrapper-csvofthedata.py)
Uses requests and BeautifulSoup to fetch review pages for a product.

Extracts review text and date, filtering for recent reviews.

Applies TextBlob sentiment analysis to each review.

Appends sentiment and confidence scores.

Saves the enriched data to CSV.

