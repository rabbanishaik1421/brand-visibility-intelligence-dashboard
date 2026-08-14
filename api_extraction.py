import pandas as pd
import requests

# API Extraction
from api import api_key
api_key = api_key()

url = "https://serpapi.com/search?engine=google_shopping"

KEYWORDS = ["Smart Phone", "Washing Machine", "laptop", "headphones", "smartwatch", "tablet", "gaming laptop", 
"wireless earbuds", "Bluetooth speaker", "camera"]

products = []

for keyword in KEYWORDS:    
  params = {
    "engine": "google_shopping",
    "q": keyword,
    "location": "India",
    "api_key": api_key
  }

  response = requests.get(url, params=params)
  data = response.json()

  for item in data.get("shopping_results", []):
    original_price = item.get("price")
    selling_price = item.get("extracted_price")

    discount = None

    if original_price is not None and selling_price is not None:
      try:
        original_price = float(
          str(original_price)
            .replace("$", "")
            .replace("₹", "")
            .replace(",", "")
        )

        selling_price = float(selling_price)

        if original_price > selling_price and original_price > 0:
          discount = ((original_price - selling_price) / original_price) * 100

      except (ValueError, TypeError):
        discount = None

      products.append({
        "keyword":keyword,
        "title":item.get("title"),
        "price":item.get("extracted_price"),
        "rating":item.get("rating"),
        "reviews":item.get("reviews"),
        "platform":item.get("source"),
        "position":item.get("position"),
        "delivery":item.get("delivery"),
        "discount": discount
      })

# print(products)

# Convert list of dictionaries into DataFrame
df = pd.DataFrame(products)
# print(df)

# Save DataFrame to CSV
df.to_csv("api_data.csv", index=False)

# print("Data saved successfully!")
print(f"Total products: {len(df)}")