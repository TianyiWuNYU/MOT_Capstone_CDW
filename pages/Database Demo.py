import streamlit as st
import pandas as pd

@st.cache  # You might remove allow_output_mutation if you follow this strategy
def load_data_from_github(url):
    return pd.read_csv(url)

# Load data and immediately create a copy for operations
github_raw_url = 'https://raw.githubusercontent.com/TianyiWuNYU/test/main/data/cdw_csv_processed.csv'
data = load_data_from_github(github_raw_url).copy()

small_table = data[['generator_name']].copy()
small_table.reset_index(inplace=True)

search_query = st.text_input("Search by generator name:")

if search_query:
    filtered_table = small_table[small_table['generator_name'].str.contains(search_query, case=False, na=False)].copy()
else:
    filtered_table = small_table.copy()

st.write("Table for `index` and `generator_name`:")
st.dataframe(filtered_table)

if not filtered_table.empty:
    selected_index = st.selectbox("Select an index to see details", filtered_table['index'])
    st.write("Details at selected index:")
    st.write(data.iloc[selected_index])
else:
    st.write("No results found.")
