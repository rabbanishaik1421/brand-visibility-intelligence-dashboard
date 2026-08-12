import streamlit as st
from kpi_cards import show_kpi_cards, show_brand_kpi_cards, show_pricing_anaysis_kpi_cards, show_platform_analysis_kpi_cards, show_visibility_ranking_kpi_cards
from common import show_products_explorer

def show_tabs(df):

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "Overview",
        "Brand Insight",
        "Pricing Analysis",
        "Platform Analysis",
        "Visibility & Ranking",
        "Products Explorer"
    ])

    with tab1:
        st.header("Overview")

        show_kpi_cards(df)        
        # st.dataframe(df)

    with tab2:
        st.header("Brand Insight")
        show_brand_kpi_cards(df)

    with tab3:
        st.header("Pricing Analysis")
        show_pricing_anaysis_kpi_cards(df)

    with tab4:
        st.header("Platform Analysis")
        show_platform_analysis_kpi_cards(df)

    with tab5:
        st.subheader("Visibilty & Ranking")
        show_visibility_ranking_kpi_cards(df)

    # Product Explorer tab
    with tab6:
        st.subheader("Products Explorer")
        show_products_explorer(df)