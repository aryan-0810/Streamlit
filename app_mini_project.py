import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Product Rating Analyzer",
    layout="wide"
)

st.title("Flipkart Product Rating Analyzer")

if "products" not in st.session_state:
    st.session_state.products = pd.DataFrame({
        "Product": [
            "iPhone 15",
            "Samsung Galaxy S24",
            "OnePlus 12",
            "Sony Headphones",
            "Boat Earbuds",
            "Dell Laptop",
            "HP Laptop",
            "Nike Shoes",
            "Adidas Shoes",
            "Canon Camera"
        ],
        "Category": [
            "Mobiles",
            "Mobiles",
            "Mobiles",
            "Electronics",
            "Electronics",
            "Laptops",
            "Laptops",
            "Fashion",
            "Fashion",
            "Cameras"
        ],
        "Rating": [
            4.6,
            4.5,
            4.4,
            4.3,
            4.1,
            4.5,
            4.2,
            4.4,
            4.3,
            4.6
        ]
    })

with st.sidebar:
    st.header("Filters")

    uploaded_file = st.file_uploader(
        "Upload Product CSV",
        type=["csv"]
    )

    if uploaded_file is not None:
        try:
            products = pd.read_csv(uploaded_file)

            required_columns = ["Product", "Category", "Rating"]

            if all(column in products.columns for column in required_columns):
                st.session_state.products = products
                st.success("CSV uploaded successfully.")
            else:
                st.error("CSV must contain Product, Category, and Rating columns.")

        except Exception:
            st.error("Unable to read the uploaded CSV file.")

products = st.session_state.products

categories = ["All Categories"] + sorted(
    products["Category"].dropna().astype(str).unique().tolist()
)

selected_category = st.sidebar.selectbox(
    "Select Product Category",
    categories
)

if selected_category == "All Categories":
    filtered_products = products
else:
    filtered_products = products[
        products["Category"].astype(str) == selected_category
    ]

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Products",
        len(filtered_products)
    )

with col2:
    average_rating = filtered_products["Rating"].mean()

    st.metric(
        "Average Rating",
        f"{average_rating:.2f}" if not pd.isna(average_rating) else "N/A"
    )

with col3:
    if len(filtered_products) > 0:
        highest_rating = filtered_products["Rating"].max()
        st.metric(
            "Highest Rating",
            f"{highest_rating:.1f}"
        )
    else:
        st.metric("Highest Rating", "N/A")

st.subheader("Product Results")

if filtered_products.empty:
    st.warning("No products found for the selected category.")
else:
    st.dataframe(
        filtered_products,
        use_container_width=True
    )

    st.subheader("Rating Analysis")

    rating_data = (
        filtered_products
        .groupby("Category")["Rating"]
        .mean()
    )

    st.bar_chart(rating_data)

with st.expander("Advanced Options"):
    minimum_rating = st.slider(
        "Minimum Rating",
        min_value=0.0,
        max_value=5.0,
        value=0.0,
        step=0.1
    )

    advanced_data = filtered_products[
        filtered_products["Rating"] >= minimum_rating
    ]

    st.write("Products matching minimum rating:")
    st.dataframe(
        advanced_data,
        use_container_width=True
    )