import streamlit as st
import pandas as pd

def show_kpi_cards(df):
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.metric("Total Products", len(df), border=True)

    with col2:
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

    # with col3:
    #     st.metric("%Discounted Price", "Discounted Price", border=True)

def show_platform_analysis_kpi_cards(df):
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Platforms", df["platform"].dropna().count(), border=True)

    with col2:
        avg_rating_by_platform = df.groupby("platform")["rating"].mean()

        best_platform = avg_rating_by_platform.idxmax()
        st.metric("Best Platfrom", best_platform, border=True)

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