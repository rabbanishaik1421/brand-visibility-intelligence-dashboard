import pandas as pd
import streamlit as st
from database import get_connection
from common import page_header

# Fetch data from the cleaned dataset
brand_dataset = pd.read_csv("brand_cleaned_dataset.csv")
df = pd.DataFrame(brand_dataset)
# print(df)

st.set_page_config(
    page_title="Brand Visibility Intelligence Dashbaord",
    layout="wide"
)

page_header()

con = get_connection()
bd = pd.read_sql("SELECT * FROM brand_dashboard_data", con)
st.dataframe(bd)