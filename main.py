import pandas as pd
import streamlit as st

# Fetch data from the cleaned dataset
brand_dataset = pd.read_csv("brand_cleaned_dataset.csv")
df = pd.DataFrame(brand_dataset)
# print(df)

st.title("Brand Visibility Intelligence Dashboard")

