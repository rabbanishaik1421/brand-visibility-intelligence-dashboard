import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def show_overview_charts(df):
    col1, col2 = st.columns(2)

    with col1:
        st.text("Price Distribution")
        # Price deistribution - Histogram
        fig1, ax1 = plt.subplots()

        ax1.hist(
            df["price"].dropna(),
            bins=20
        )

        ax1.set_title("Price Distribution")
        ax1.set_xlabel("Price")
        ax1.set_ylabel("Number of plots")

        st.pyplot(fig1)
        plt.close(fig1)

    with col2:
        # Products Per Keyword (Bar Chart)

        st.text("Products per keyword")

        products_keyword = (df["keyword"].dropna().value_counts())

        fig2, ax2 = plt.subplots()

        ax2.bar(
            products_keyword.index,
            products_keyword.values
        )

        ax2.set_title("Products per keyword")
        ax2.set_xlabel("Keyword")
        ax2.set_ylabel("Products count")

        plt.xticks(rotation=45, ha="right")

        st.pyplot(fig2)
        plt.close(fig2)
    
    col3, col4 = st.columns(2)

    # Platform share (Pie chart)
    with col3:
        platform_count = (df["platform"].dropna().value_counts().sort_values(ascending=False).head(8))

        fig3, ax3 = plt.subplots()

        ax3.pie(
            platform_count.values,
            labels=platform_count.index,
            autopct="%1.1f%%"
        )

        ax3.set_title("Platform share")

        st.pyplot(fig3)
        plt.close(fig3)

# Brand vs product chart function
def show_brand_v_product(df):
    brand_counts = (
        df["brand"].dropna().value_counts().head(10)
    )

    fig, ax = plt.subplots()

    ax.bar(
        brand_counts.index,
        brand_counts.values
    )

    ax.set_title("Brand vs Product")
    ax.set_xlabel("Brand")
    ax.set_ylabel("Products count")

    plt.xticks(rotation=45, ha="right")

    st.pyplot(fig)

    plt.close(fig)

# Brand vs average rating
def show_brand_vs_averating_rating(df):
    brand_rating = (
        df.dropna(subset=["brand", "rating"])
            .groupby("brand")["rating"]
            .mean()
            .sort_values(ascending=False)
            .head(10)
    )

    fig, ax = plt.subplots()

    ax.bar(
        brand_rating.index,
        brand_rating.values
    )

    ax.set_title("Brand vs Average Rating")
    ax.set_xlabel("Brand")
    ax.set_ylabel("Average Rating")

    plt.xticks(rotation=90,  ha="right")

    st.pyplot(fig)
    plt.close(fig)

# Brand Insight: Top brands on top 10 positions
def show_top_brands_top_positions(df):
    top_ten_positions = df[
        df["position"].between(1, 10)
    ]

    # print(top_ten_positions)
    top_brands = (
        top_ten_positions["brand"]
        .dropna()
        .value_counts()
        .head(10)
    )
    # print(top_brands)

    fig, ax = plt.subplots()

    ax.bar(
        top_brands.index,
        top_brands.values
    )

    ax.set_title("Top brands on top 10 positions")
    ax.set_xlabel("Brands")
    ax.set_ylabel("Position")

    st.pyplot(fig)

    plt.close(fig)