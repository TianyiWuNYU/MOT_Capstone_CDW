import streamlit as st
import pandas as pd
import copy

@st.cache
def load_data_from_github(url):
    return pd.read_csv(url)

github_raw_url = 'https://raw.githubusercontent.com/TianyiWuNYU/test/main/data/cdw_csv_processed.csv'
data = load_data_from_github(github_raw_url)

# Make a deep copy of data for manipulation
small_table = copy.deepcopy(data[['generator_name']])
small_table.reset_index(inplace=True)

search_query = st.text_input("Search by generator name:")

if search_query:
    # Use a deep copy to filter data
    filtered_table = copy.deepcopy(small_table[small_table['generator_name'].str.contains(search_query, case=False, na=False)])
else:
    filtered_table = copy.deepcopy(small_table)

st.write("Table for `index` and `generator_name`:")
st.dataframe(filtered_table)

if not filtered_table.empty:
    selected_index = st.selectbox("Select an index to see details", filtered_table['index'])
    st.write("Details at selected index:")
    st.write(data.iloc[selected_index])
else:
    st.write("No results found.")
