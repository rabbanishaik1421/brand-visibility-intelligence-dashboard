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

# Price distribution
def show_pricing_analysis_price_distribution(df):
    col1, col2 = st.columns(2)

    with col1:
        st.badge("Price Distribution")
        price_data = df["price"].dropna()

        fig, ax = plt.subplots(figsize=(10, 6))

        ax.hist(
            price_data,
            bins=20
        )           
        ax.set_title("Price Distribution")
        ax.set_xlabel("Price")
        ax.set_ylabel("Number of Products")

        st.pyplot(fig)

        plt.close(fig)

    with col2:
        st.badge("Price vs Ranking")
        price_ranking_data = (
            df.dropna(subset=["brand", "position"])
        )

        fig, ax = plt.subplots(figsize=(10, 6))

        ax.scatter(
            price_ranking_data["price"],
            price_ranking_data["position"],
            alpha=0.6        
        )

        ax.set_title("Price vs Ranking")
        ax.set_xlabel("Price")
        ax.set_ylabel("Ranking")

        st.pyplot(fig)
        plt.close(fig)             

    col3, col4 = st.columns(2)   

    with col3:
        st.badge("Price Vs Rating")
        price_rating_data = (
            df.dropna(subset=["price", "rating"])
        )

        fig, ax = plt.subplots(figsize=(10,6))

        ax.scatter(
            price_rating_data["price"],
            price_rating_data["rating"],
            alpha=0.5
        )

        ax.set_title("Price vs Rating")
        ax.set_xlabel("Price")
        ax.set_ylabel("Rating")

        st.pyplot(fig)

        plt.close(fig)

# Platoform Analysis
def show_platform_analysis_charts(df):
    col1, col2 = st.columns(2)

    # Platform vs product count
    with col1:
        st.text("Platform vs Products Count")
        platform_products = (
            df["platform"].dropna().value_counts().head(10)
        )

        fig, ax = plt.subplots(figsize=(10, 6))

        ax.barh(
            platform_products.index,
            platform_products.values
        )

        ax.set_title("Platform vs Products Count")
        ax.set_xlabel("Platform")
        ax.set_ylabel("Products Count")

        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()

        st.pyplot(fig)
        plt.close(fig)

    # Platform vs Average Price
    with col2:
        st.text("Platform vs Average Price")

        platform_price = (
            df.dropna(subset=["platform", "price"])
            .groupby("platform")["price"]
            .mean()
            .sort_values(ascending=False)
            .head(10)
        )

        fig, ax = plt.subplots(figsize=(10, 6))

        ax.bar(
            platform_price.index,
            platform_price.values
        )

        ax.set_title("Platform vs Average Price")
        ax.set_xlabel("Platform")
        ax.set_ylabel("Average Price")

        plt.xticks(rotation=45, ha="right")

        st.pyplot(fig)
        plt.close(fig)


    col3, col4 = st.columns(2)
    # Platform vs AVG Rating
    with col3:        
        st.text("Platfrom vs Average Rating")

        platform_rating = (
            df.dropna(subset=["platform", "rating"]).groupby("platform")["rating"].mean().sort_values(ascending=False).head(10)
        )

        fig, ax = plt.subplots(figsize=(10, 6))

        ax.bar(
            platform_rating.index,
            platform_rating.values
        )

        ax.set_title("Platform vs AVG Rating")
        ax.set_xlabel("Platform")
        ax.set_ylabel("AVG Rating")

        plt.xticks(rotation=45, ha="right")

        st.pyplot(fig)
        plt.close(fig)

# Visibility & Ranking
def show_visibility_ranking_charts(df):
    col1, col2 = st.columns(2)

    with col1:
        st.text("Ranking Distribution")

        # Ranking deistribution - Histogram
        ranking_data = df["position"].dropna()

        fig, ax = plt.subplots(figsize=(10, 6))

        ax.hist(
            ranking_data,
            bins=20
        )

        ax.set_title("Ranking Distribution")
        ax.set_xlabel("Position")
        ax.set_ylabel("Number of Products")

        plt.tight_layout()

        st.pyplot(fig)

        plt.close(fig)

    # Rating vs Ranking
    with col2:
        # Rating vs Ranking
        st.text("Rating vs Ranking")

        chart_df = df.dropna(
            subset=["rating", "position"]
        )

        fig, ax = plt.subplots(figsize=(10, 6))

        ax.scatter(
            chart_df["rating"],
            chart_df["position"],
            alpha=0.9
        )

        ax.set_title("Rating vs Ranking")
        ax.set_xlabel("Rating")
        ax.set_ylabel("Position")

        # Position 1 should appear at the top
        ax.invert_yaxis()

        plt.tight_layout()

        st.pyplot(fig)

        plt.close(fig)

    col3, col4 = st.columns(2)

    # Reviews vs Ranking - Bubble Chart
    with col3:
        st.text("Reviews vs Ranking")

        chart_df = df.dropna(
            subset=["reviews", "position"]
        )

        fig, ax = plt.subplots(figsize=(10, 6))

        ax.scatter(
            chart_df["reviews"],
            chart_df["position"],
            s=chart_df["reviews"],
            alpha=0.5
        )

        ax.set_title("Reviews vs Ranking")
        ax.set_xlabel("Reviews")
        ax.set_ylabel("Position")

        ax.invert_yaxis()

        plt.tight_layout()

        st.pyplot(fig)

        plt.close(fig)