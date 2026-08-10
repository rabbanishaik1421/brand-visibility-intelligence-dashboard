from database import get_connection
import pandas as pd

con = get_connection()
cursor = con.cursor()

cursor.execute(
    """
CREATE TABLE IF NOT EXISTS brand_dashboard_data (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    keyword TEXT,
    title TEXT,
    price REAL,
    rating REAL,
    reviews REAL,
    platform TEXT,
    position INTEGER,
    delivery TEXT,
    brand TEXT
)
"""
)

brand_dat = pd.read_csv("brand_cleaned_dataset.csv")

for _,row in brand_dat.iterrows():
    cursor.execute(
        """
        INSERT INTO brand_dashboard_data(keyword, title, price, rating, reviews, platform, position, delivery, brand) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (row["keyword"], row["title"], row["price"], row["rating"], row["reviews"], row["platform"], row["position"], row["delivery"], row["brand"])
    )

con.commit()