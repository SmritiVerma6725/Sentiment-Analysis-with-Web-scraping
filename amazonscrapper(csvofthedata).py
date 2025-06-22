import requests           #amazon scrapper
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import pandas as pd
import traceback
import csv

cookies = {
    'session-id': '258-4465433-4676101',
    'ubid-acbin': '261-3422590-8166335',
    'sst-acbin': 'Sst1|PQEf5PYkSs9hRLJ6UV3sesGvB2AqPhzIKH9ykRIWQy8Yl64DC0i3w4lQ3nOBnaV9B4WS7Hik6xPQNrcw6JWPvzKyw9WUfyVWoy_yhkGqDY5p8JWHPN4ow_EGl-9ibwJmZ6lFAyxRVBBWaCp7qd86xv_wqZoUenAsuWu-hgVM8XVWDnjO465YciBi-Jzbh6lFAsljLlz5wKDV22X6DVSZPMb_jHotgNkWxd2clhWtsJf_3bQY8-CnyDuACcsfT_vVmQZY',
    'session-id-time': '2082787201l',
    'i18n-prefs': 'INR',
    'lc-acbin': 'en_IN',
    'session-token': 'MFQPJ8eSbukoA5vIWCvihriB/Lw/EP9wRVNxBKNt+Q88KWBG0DWqVG1+EjY8OMWWy360cCWw1VGC4fEauwZr/3P4YYDQVmZYqu+9vGfBJbc9XM3rEAVhz/158cgVwlCdDWglG+2ac5LYb5XKDKciCyYojmfZ4pDxrfC567eQH3gWI8ChDJqJSLZaAFlq5tUlRkBHm/7ymQrdR2s/gl18mZis8E46LC8UoJOvJWkNOsENEYef1qA5E/5Ue0eemwgzHJFu2CZPFPL61Q6DZO1hT/1WXzLUnb2lVwsYePMqInEQ7TcH2UF7AZ4zj5Q5HlqvAehC/Ia4b9C1iHNInoGUPYpwBsje7p01',
    'csm-hit': 'tb:s-G2XDGE27R7QPM3D9619H|1719308435358&t:1719308436459&adb:adblk_no',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'device-memory': '8',
    'downlink': '10',
    'dpr': '1.5',
    'ect': '4g',
    'priority': 'u=0, i',
    'referer': 'https://www.amazon.in/',
    'rtt': '50',
    'sec-ch-device-memory': '8',
    'sec-ch-dpr': '1.5',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"15.0.0"',
    'sec-ch-viewport-width': '1280',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'viewport-width': '1280',
}
proxies = {"proxies removed"}
page = 1
product_code = input("Enter your url ")
lst = []

# B0C4YRBB8Z
flag = True
temp_df = {"Review":[   ],
           "Date":[],
           }

while flag:  
    api = f'https://www.amazon.in/product-reviews/{product_code}/ref=cm_cr_arp_d_viewopt_srt?sortBy=recent&pageNumber={page}'
    print('API', api)                          #infinite loop
    response = requests.get(api, cookies=cookies, headers=headers,proxies=proxies, verify = False)
    print("Response code", response)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    data_class = soup.select('div.a-section.celwidget')        #select all the text and select_one will only selct one text
    for data in data_class:
        try:
            review = data.select_one('div.a-row.a-spacing-small.review-data').text
            date_str = data.select_one('span.a-size-base.a-color-secondary.review-date').text.replace('Reviewed in India on ','')
            date_obj = datetime.strptime(date_str, "%d %B %Y")
            # print(date_obj)
            current_date = datetime.now()   
            difference = current_date - date_obj
            if difference < timedelta(days=5):
                print(review)
                temp_df['Review'].append(review)
                temp_df['Date'].append(date_obj)
            else:
                flag = False
                break
        except:
            print("Error", traceback.format_exc())
    page = page + 1

df = pd.DataFrame(temp_df)
df.to_csv("dsduscu.csv", index=False)

import pandas as pd
from textblob import TextBlob

# Read the CSV file into a DataFrame
df = pd.read_csv('dsduscu.csv')

# Print the DataFrame
print(df)

def analyze_sentiment_with_confidence(review):
    # Check if the review is a string; otherwise, return 'neutral' with 0 confidence
    if isinstance(review, str):
        analysis = TextBlob(review)
        polarity = analysis.sentiment.polarity
        if polarity > 0:
            sentiment = 'positive'
        elif polarity < 0:
            sentiment = 'negative'
        else:
            sentiment = 'neutral'
        confidence = abs(polarity)  # Confidence score based on polarity
        return sentiment, confidence
    else:
        return 'neutral', 0 

# Apply the sentiment analysis function to the 'review' column, handling NaNs
df[['sentiment', 'confidence']] = df['Review'].apply(
    lambda x: pd.Series(analyze_sentiment_with_confidence(x)) if pd.notnull(x) else pd.Series(['neutral', 0])
)
# Save the DataFrame to a new CSV file
df.to_csv("dsduscu.csv", index=False)




# # print(ls)

# from textblob import TextBlob


# def analyze_sentiment(text):
#     analysis = TextBlob(text)

#     # Check sentiment polarity
#     if analysis.sentiment.polarity > 0:
#         return 'Positive'
#     elif analysis.sentiment.polarity == 0:
#         return 'Neutral'
    
#     else:
#         return 'Negative'


# # # Example usage
# # ls.append('I hated this product')
# # for text in ls:
# #     analyze_sentiment(text)
# #     print(text,'--------->', analyze_sentiment(text))
# #     print('#######################')
# import requests
# from bs4 import BeautifulSoup

# def scrape_amazon_product(url):
#     headers = {
#         'User-Agent': 'Your User-Agent String'  # Set a proper User-Agent to avoid getting blocked
#     }
#     response = requests.get(url, headers=headers)
    
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.content, 'html.parser')
        
#         # Example: Extracting product title
#         title_element = soup.find('span', {'id': 'productTitle'})
#         if title_element:
#             title = title_element.get_text().strip()
#         else:
#             title = None
        
#         # Example: Extracting product price
#         price_element = soup.find('span', {'id': 'priceblock_ourprice'})
#         if price_element:
#             price = price_element.get_text().strip()
#         else:
#             price = None
        
#         # Example: Extracting product description
#         description_element = soup.find('div', {'id': 'productDescription'})
#         if description_element:
#             description = description_element.get_text().strip()
#         else:
#             description = None
        
#         # Calculate confidence score based on presence of key elements
#         confidence_score = 0
        
#         if title:
#             confidence_score += 30
#         if price:
#             confidence_score += 30
#         if description:
#             confidence_score += 40
        
#         return {
#             'title': title,
#             'price': price,
#             'description': description,
#             'confidence_score': confidence_score
#         }
#     else:
#         print(f"Failed to fetch URL: {url}")
#         return None

# # Example usage:
# amazon_url = 'https://www.amazon.com/dp/B07VGRJDFY/'
# product_data = scrape_amazon_product(amazon_url)
# if product_data:
#     print("Product Title:", product_data['title'])
#     print("Product Price:", product_data['price'])
#     print("Product Description:", product_data['description'])
#     print("Confidence Score:", product_data['confidence_score'])

 