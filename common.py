import streamlit as st
import pandas as pd

def page_header():
    st.markdown(
        """
        <div class="bd-title">
            <h3>Brand Visibility Intelligence Dashboard</h3>
        </div>
    """, unsafe_allow_html=True
    )

def categorize_price_ranges(price):
    if price <= 5000:
        return "Budget"
    elif price <= 20000:
        return "Mid-Range"
    elif price <= 50000:
        return "Premium" 
    else:
        return "Luxury"

import streamlit as st


def show_products_explorer(df):

    # Search Input
    search_text = st.text_input(
        "Search Product",
        placeholder="Enter product title to search product"
    )

    products_df = df.copy()

    # Search by product title
    if search_text:
        products_df = products_df[
            products_df["title"].str.contains(
                search_text,
                case=False,
                na=False
            )
        ]

    # Columns to display
    display_columns = [
        "title",
        "brand",
        "price",
        "rating",
        "reviews",
        "platform",
        "position",
    ]

    products_df = products_df[display_columns]

    # Rename columns
    products_df = products_df.rename(
        columns={
            "title": "Title",
            "brand": "Brand",
            "price": "Price",
            "rating": "Rating",
            "reviews": "Reviews",
            "platform": "Platform",
            "position": "Position",
        }
    )

    # Display sortable table
    st.dataframe(
        products_df,
        width="stretch",
        hide_index=True
    )