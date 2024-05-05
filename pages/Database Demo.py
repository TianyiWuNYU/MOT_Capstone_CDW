import streamlit as st
import pandas as pd

@st.cache
def load_data_from_github(url):
    return pd.read_csv(url)

# Load data
github_raw_url = 'https://raw.githubusercontent.com/TianyiWuNYU/test/main/data/cdw_csv_processed.csv'
data = load_data_from_github(github_raw_url)

# Ensure generator_name is a string and handle NaN values
data['generator_name'] = data['generator_name'].fillna('').astype(str)

small_table = data[['generator_name']].copy()
small_table.reset_index(inplace=True)

# Display a simple text search field
search_query = st.text_input("Search by generator name:")

# Filter data based on search input
if search_query:
    filtered_table = small_table[small_table['generator_name'].str.contains(search_query, case=False, na=False)]
else:
    filtered_table = small_table

st.write("Table for `index` and `generator_name`:")
st.dataframe(filtered_table)

# Select an index from the filtered results
if not filtered_table.empty:
    selected_index = st.selectbox("Select an index to see details", filtered_table['index'])
    st.write("Details at selected index:")
    st.write(data.iloc[selected_index])
else:
    st.write("No results found.")
