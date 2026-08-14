import pandas as pd
from common import categorize_price_ranges

# CSV Extraction
csv_data = pd.read_csv("brand_dirty_dataset.csv")
csv_df = pd.DataFrame(csv_data)

# API CSV Data Extraction
api_data = pd.read_csv("api_data.csv")
api_df = pd.DataFrame(api_data)

final_columns = [
    "keyword",
    "title",
    "price",
    "rating",
    "reviews",
    "platform",
    "position",
    "delivery",
    "discount"
]

# Standardize column names
csv_df.columns = csv_df.columns.str.strip().str.lower()
api_df.columns = api_df.columns.str.strip().str.lower()

# Rename columns
api_df = api_df.rename(columns={
    "source": "platform",
})

# Add missing column to CSV dataset
csv_df["position"] = None
csv_df["discount"] = None

# Select common columns
csv_df = csv_df[final_columns]
api_df = api_df[final_columns]

# Combine datasets
df = pd.concat(
    [csv_df, api_df],
    ignore_index=True
)

# Clean platform
df["platform"] = (
    df["platform"]
    .astype("string")
    .str.strip()
    .str.lower()
    .str.title()
)

df["title"] = (
    df["title"]
    .astype("string")
    .str.strip()
    .str.lower()
    .str.title()
)

# Clean price
df["price"] = pd.to_numeric(
    df["price"],
    errors="coerce"
)

# Remove duplicates
df = df.drop_duplicates(
    subset=["keyword", "title", "platform", "price"]
)

# Clean reviews
df["reviews"] = (
    df["reviews"]
    .astype("string")
    .str.strip()
    .replace("", pd.NA)
)

# Convert numeric columns
df["rating"] = pd.to_numeric(
    df["rating"],
    errors="coerce"
)

df["reviews"] = pd.to_numeric(
    df["reviews"],
    errors="coerce"
)

df["position"] = df["position"].astype("Int64")

df = df.dropna(subset=["price"])

#Delivery values be filled or labeled as “Unknown”?
df["delivery"] = (
    df["delivery"]
    .astype("string")
    .str.strip()
    .fillna("Unknown")
)

# Remove the negative values
df = df[df["price"] > 0]

# Removed the noisy data from the title column (e.g., “!!!”)?
df["title"] = (df["title"].str.replace("!!!", "", regex=False).str.strip())

# Platform names are conistant
df["platform"] = (
    df["platform"]
    .astype("string")
    .str.strip()
    .str.lower()
    .str.title()
)

# Standardized the keyword
df["keyword"] = df["keyword"].str.lower()

df["delivery"] = (
    df["delivery"]
    .astype("string")
    .str.strip()
    .str.replace(r"\s+", " ", regex=True)
)


df = df.drop_duplicates(
    subset=["keyword", "title", "platform", "price"],
    keep="first"
)

# brand extraction from title improve the dataset?
df["brand"] = (
    df["title"]
    .astype("string")
    .str.strip()
    .str.split()
    .str[0]
)

# Create Visibility Score
df["visibility_score"] = 1 / df["position"]

# Categorize price ranges
df["price_range"] = df["price"].apply(categorize_price_ranges)

df.to_csv("brand_cleaned_dataset.csv", index=False)


