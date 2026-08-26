import streamlit as st
import pandas as pd

st.title("CSV Data Explorer")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.header("Complete Dataset")
    st.dataframe(df)

    st.header("Top 10 Rows")
    st.dataframe(df.head(10))

    st.write("Total Rows:", df.shape[0])
    st.write("Total Columns:", df.shape[1])

    st.header("Select a Column")

    selected_column = st.selectbox(
        "Choose a column",
        df.columns
    )

    st.dataframe(df[[selected_column]])

    st.header("Search Dataset")

    search_term = st.text_input("Enter a search term")

    if search_term:
        filtered_df = df[
            df.apply(
                lambda row: row.astype(str).str.contains(
                    search_term,
                    case=False,
                    na=False
                ).any(),
                axis=1
            )
        ]

        st.write("Search Results")
        st.dataframe(filtered_df)