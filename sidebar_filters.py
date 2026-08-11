import streamlit as st
import pandas as pd

def show_sidebar_filter(df):
    st.sidebar.header("Filters")

    price_data = df["price"].dropna()

    min_price = float(price_data.min())
    max_price = float(price_data.max())

    rating_data = df["rating"].dropna()
    min_rating = float(rating_data.min())
    max_rating = float(rating_data.max())

    # keyword filter
    keyword_filter = st.sidebar.selectbox(
        "Keyword",
        df["keyword"].dropna().unique(),
        index=None
    )
    
    # Brand Filter
    brand_filter = st.sidebar.selectbox(
        "Brand",
        options=df["brand"].dropna().unique(),
        index=None
    )

    # Platform Filter
    platform_filter = st.sidebar.selectbox(
        "Platform",
        options=df["platform"].dropna().unique(),
        index=None
    )

    # Price Range / Price Range slider
    price_range_filter = st.sidebar.slider(
        "Price Range",
        min_value=min_price,
        max_value=max_price,
        value = (min_price, max_price),
        step=1000.0
    )

    # rating range slider
    if len(rating_data) > 0:
        rating_range_filter = st.sidebar.slider(
            "Rating Range",
            min_value = min_rating,
            max_value = max_rating,
            value = (min_rating, max_rating),
            step = 1.0
        )
    else:
        rating_range_filter = None

    # position filter
    position_filter = st.sidebar.selectbox(
        "Position",
        df["position"].dropna().unique(),
        index=None
    )

    filter_df = df.copy()
    filter_df["rating"] = pd.to_numeric(
        filter_df["rating"],
        errors="coerce"
    )
    if keyword_filter:
        filter_df = filter_df[
            filter_df["keyword"] == keyword_filter
        ]

    if brand_filter:
        filter_df = filter_df[
            filter_df["brand"] == brand_filter
        ]

    if platform_filter:
        filter_df = filter_df[
            filter_df["platform"] == platform_filter
        ]

    if price_range_filter:
        filter_df = filter_df[
            filter_df["price"].between(float(price_range_filter[0]), float(price_range_filter[1]))
        ]

    if rating_range_filter:
        filter_df = filter_df[
            filter_df["rating"].between(float(rating_range_filter[0]), float(rating_range_filter[1]))
        ]

    if position_filter:
        # print(position_filter)
        filter_df = filter_df[
            filter_df["position"] == int(position_filter)
        ]
        

    return filter_df