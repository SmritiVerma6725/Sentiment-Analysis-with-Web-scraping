from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome()
query = "laptop"
file = 0
data = []

for i in range(1, 2):
    driver.get(f"https://www.amazon.in/s?k={query}&page={i}")
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    items = soup.select("div.puis-card-container")
    print(f"{len(items)} items found")
    for tags in items:
        item_data = {}
        try:
            title = tags.select_one("h2.a-size-mini.a-spacing-none.a-color-base.s-line-clamp-2").get_text(strip=True)
            print("Title:", title)
            item_data["Title"] = title
        except Exception as e:
            print(f"Title not found: {e}")
            item_data["Title"] = ""

        try:
            MRP = tags.select_one("span.a-price.a-text-price span").get_text(strip=True)
            print("MRP:", MRP)
            item_data["MRP"] = MRP
        except Exception as e:
            print(f"MRP not found: {e}")
            item_data["MRP"] = ""

        try:
            ASP = tags.select_one("span.a-price-whole").get_text(strip=True)
            print("ASP:", ASP)
            item_data["ASP"] = ASP
        except Exception as e:
            print(f"ASP not found: {e}")
            item_data["ASP"] = ""

        try:
            Rating = tags.select_one("a.a-popover-trigger.a-declarative").get_text(strip=True)
            print("Rating:", Rating)
            item_data["Rating"] = Rating
        except Exception as e:
            print(f"Rating not found: {e}")
            item_data["Rating"] = ""

        print("Item data:", item_data)  # Debugging print to check the item data before appending
        data.append(item_data)

driver.close()

# Print the collected data for debugging
print("Collected data:", data)

# Check if data is not empty
if data:
    df = pd.DataFrame(data)
    print("DataFrame created:")
    print(df)
    try:
        df.to_csv('amazon_laptops.csv', index=False)
        print("CSV file 'amazon_laptops.csv' created successfully.")
    except Exception as e:
        print(f"Failed to write CSV file: {e}")
else:
    print("No data collected")
