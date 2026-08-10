import streamlit as st

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