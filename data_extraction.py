import pandas as pd

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

# -------------------------------
# DATA VALIDATION
# -------------------------------

# 1. What is the total number of rows and columns in the dataset?
# print("Dataset Shape:", df.shape)

# 2. What are the data types of each column?
# df.info()

# 3.	Which columns are expected to be numeric but are not?
# print(df[["price", "rating", "reviews", "position"]].dtypes)

# 4.Which columns contain missing values?
# print("\nMissing Values:")
# print(df.isna().sum())

# print(df[df["price"].isna()])

# 5.	What is the percentage of missing data in each column?
missing_report = pd.DataFrame({
    "Missing_Count": df.isna().sum(),
    "Missing_Percentage": (df.isna().mean() * 100).round(2)
})

# print(missing_report)
# 7. Should missing delivery values be filled or labeled as “Unknown”?
df["delivery"] = (
    df["delivery"]
    .astype("string")
    .str.strip()
    .fillna("Unknown")
)

# print(df["delivery"].isna().sum())

# 8. Are there columns with incorrect data types (e.g., price as text)?
# print(df.dtypes)

# 9. How do you convert columns like price and reviews into numeric format safely?
# print(df[["price", "rating", "reviews"]].dtypes)

# 11. Are there duplicate rows in the dataset?
# print("Duplicate rows:", df.duplicated().sum())

# 12. What criteria should define a duplicate record (e.g., title + price)?

# 13.	How many duplicate records exist, and how should they be handled?
# df = df.drop_duplicates(
#     subset=["keyword", "title", "platform", "price"]
# )
# print(df.shape)

# 14.	Are there any negative or zero values in the price column?
# zero_prices = df[df["price"] == 0]
# negative_prices = df[df["price"] < 0]

# print("Zero price records:", len(zero_prices))
# print("Negative price records:", len(negative_prices))

# negative_prices = df[df["price"] < 0]

# print(negative_prices)
# Removing negative prices
# df = df[df["price"] > 0]
# zero_prices = df[df["price"] == 0]
# negative_prices = df[df["price"] < 0]

# print("Zero price records:", len(zero_prices))
# print("Negative price records:", len(negative_prices))

# 15.	Are there unrealistic or extreme values (outliers) in the dataset?
# print(df[["price", "rating", "reviews", "position"]].describe())
# Q1 = df["price"].quantile(0.25)
# Q3 = df["price"].quantile(0.75)

# IQR = Q3 - Q1

# upper_bound = Q3 + (1.5 * IQR)

# print("Upper bound:", upper_bound)

# print(
#     df[df["price"] > upper_bound][
#         ["title", "price", "platform"]
#     ]
# )

df = df[df["price"] > 0]
# print(df.shape)

# 16.	How should such invalid or inconsistent values be treated?

# 17.	What is the distribution of the price column?
# print(df.describe())
# print("Median Price:", df["price"].median())


# 18.	Are there extreme price values compared to the majority?
Q1 = df["price"].quantile(0.25)
Q3 = df["price"].quantile(0.75)

IQR = Q3 - Q1

upper_bound = Q3 + (1.5 * IQR)

extreme_prices = df[df["price"] > upper_bound]
# print("Upper bound:", upper_bound)
# print("Extreme price records:", len(extreme_prices))

# print("Negative prices:", (df["price"] < 0).sum())
# print("Zero prices:", (df["price"] == 0).sum())

# print(
#     df[df["price"] > 81864][
#         ["keyword", "title", "price", "rating", "reviews", "platform"]
#     ]
# )

# 19.	Should outliers be removed or capped? If capped, at what threshold?

# 20.	Are there unwanted characters or noise in the title column (e.g., “!!!”)?
df["title"] = (df["title"].str.replace("!!!", "", regex=False).str.strip())

# 21. How can you clean and standardize product titles?
# Converted the title

# 23. Are platform names consistent (e.g., “amazon”, “AMAZON”, “Amazon”)?
df["platform"] = (
    df["platform"]
    .astype("string")
    .str.strip()
    .str.lower()
    .str.title()
)

# 24.	How can you standardize categorical values across the dataset?
df["keyword"] = df["keyword"].str.lower()

# 25.	Are delivery values consistent and meaningful?
df["delivery"] = (
    df["delivery"]
    .astype("string")
    .str.strip()
    .str.replace(r"\s+", " ", regex=True)
)

# 26.	After cleaning, are there any remaining missing or invalid values?
# print("Remaining Missing Values:")
# print(df.isna().sum())

# print("===== FINAL DATA QUALITY CHECK =====")

# print("\nMissing values:")
# print(df.isna().sum())

# print("\nNegative prices:",
#       (df["price"] < 0).sum())

# print("Zero prices:",
#       (df["price"] == 0).sum())

# print("Invalid ratings:",
#       ((df["rating"] < 1) | (df["rating"] > 5)).sum())

# print("Negative reviews:",
#       (df["reviews"] < 0).sum())

# print("Duplicate records:",
#       df.duplicated(
#           subset=["keyword", "title", "platform", "price"]
#       ).sum())

# duplicates = df[
#     df.duplicated(
#         subset=["keyword", "title", "platform", "price"],
#         keep=False
#     )
# ]
# print(duplicates)

df = df.drop_duplicates(
    subset=["keyword", "title", "platform", "price"],
    keep="first"
)

# print(df.duplicated(
#     subset=["keyword", "title", "platform", "price"]
# ).sum())

print(df.info())

# 27.	Are all numeric columns correctly formatted and usable?
# Yes

# 28.	Does the dataset now make logical and business sense?
# 29.	Should products with no ratings or reviews be retained or removed?
# 30.	Can additional features like brand extraction from title improve the dataset?
df["brand"] = (
    df["title"]
    .astype("string")
    .str.strip()
    .str.split()
    .str[0]
)

# Final Dataset
df.to_csv("brand_cleaned_dataset.csv", index=False)

