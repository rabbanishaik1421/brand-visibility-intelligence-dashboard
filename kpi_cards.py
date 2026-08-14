import streamlit as st
import pandas as pd

def show_kpi_cards(df):
    df["price"] = pd.to_numeric(
        df["price"],
        errors="coerce"
    )

    df["rating"] = pd.to_numeric(
        df["rating"],
        errors="coerce"
    )
        
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.metric("Total Products", len(df), border=True)

    with col2:
        # print(df['price'].mean())
        st.metric("AVG Price",  f"{df['price'].mean():,.2f}", border=True)

    with col3:
        st.metric("AVG Rating",  f"{df['rating'].mean():,.2f}", border=True)

    with col4:
        st.metric("Total Reviews", f"{df["reviews"].sum():,.2f}", border=True)

    with col5:
        st.metric("Total Platform", f"{df["platform"].count()}", border=True)

def show_brand_kpi_cards(df):
    col1, col2 = st.columns(2)

    with col1:
        if df["brand"].dropna().empty:
            st.metric("Top Brand", "N/A")
        else:
            top_brand = df["brand"].value_counts().idxmax()
            st.metric("Top Brand", top_brand, border=True)

    with col2:
        visibility_score = pd.to_numeric(
            df["visibility_score"],
            errors="coerce"
        )

        avg_visibility_score = visibility_score.mean()

        if pd.isna(avg_visibility_score):
            st.metric("AVG Visibility Score", "N/A", border=True)
        else:
            st.metric(
                "AVG Visibility Score",
                f"{avg_visibility_score:.3f}",
                border=True
            )

def show_pricing_anaysis_kpi_cards(df):            
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("AVG Price", f"{df["price"].mean():,.2f}", border=True)

    with col2:
        st.metric("MAX Price", f"{df["price"].max():,.2f}", border=True)

    # Percentage Discounted Products
    with col3:

        total_products = len(df)

        discounted_products = df[
            df["discount"].notna() &
            (df["discount"] > 0)
        ]

        discounted_count = len(discounted_products)

        if total_products == 0:
            discount_percentage = 0
        else:
            discount_percentage = (
                discounted_count / total_products
            ) * 100

        st.metric(
            "% Discounted Products",
            f"{discount_percentage:.2f}%",
            border=True
        )

def show_platform_analysis_kpi_cards(df):
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        total_platforms = df["platform"].nunique()
        st.metric("Total Platforms", total_platforms, border=True)

    with col2:
        platform_data = df.dropna(
            subset=["platform", "rating"]
        )
        if platform_data.empty:
            st.metric(
                "Best Platform (Avg Rating)",
                "N/A"
            )
        else:
            avg_rating_by_platform = (
                platform_data
                .groupby("platform")["rating"]
                .mean()
            )
            # avg_rating_by_platform = df.groupby("platform")["rating"].mean()

            if avg_rating_by_platform.empty:
                st.metric(
                    "Best Platform (Avg Rating)",
                    "N/A",
                    border=True
                )
            else:

                best_platform = avg_rating_by_platform.idxmax()
                best_rating = avg_rating_by_platform.max()

                st.metric(
                    "Best Platform (Avg Rating)",
                    best_platform,
                    f"{best_rating:.2f}",
                    border=True
                )

def show_visibility_ranking_kpi_cards(df):
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        positions = df["position"].dropna()
        avg_position = positions.mean()

        if pd.isna(avg_position):
            st.metric("AVG Position", "N/A", border=True)
        else:
            st.metric(
                "AVG Visibility Score",
                f"{avg_position:.3f}",
                border=True
            )

    with col2:
        visibility_score = pd.to_numeric(
            df["visibility_score"],
            errors="coerce"
        )
        
        avg_visibility_score = visibility_score.mean()
        
        if pd.isna(avg_visibility_score):
            st.metric("AVG Visibility Score", "N/A", border=True)
        else:
            st.metric(
                "AVG Visibility Score",
                f"{avg_visibility_score:.3f}",
                border=True
            )