import pandas as pd
import streamlit as st

from database import get_connection
from common import page_header
from sidebar_filters import show_sidebar_filter
from tabs import show_tabs

st.set_page_config(
    page_title="Brand Visibility Intelligence Dashboard",
    layout="wide"
)

# Header
page_header()

# Database connection
con = get_connection()

# Retrieve dashboard data
bd = pd.read_sql(
    "SELECT * FROM brand_dashboard_data",
    con
)

# bd["visibility_score"] = pd.to_numeric(
#     bd["visibility_score"],
#     errors="coerce"
# )

# Sidebar
filtered_df = show_sidebar_filter(bd)
# st.dataframe(filtered_df)

# Show tabs
show_tabs(filtered_df)