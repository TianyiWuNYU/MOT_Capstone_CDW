import streamlit as st
import pandas as pd

@st.cache
def load_data_from_github(url):
    return pd.read_csv(url)

github_raw_url = 'https://raw.githubusercontent.com/TianyiWuNYU/test/main/data/cdw_csv_processed.csv'
data = load_data_from_github(github_raw_url)

small_table = data[['generator_name']].copy()
small_table.reset_index(inplace=True)  

st.write("table for `index` and `generator_name`：")
st.dataframe(small_table)

selected_index = st.selectbox("Select an index to see details", small_table['index'])

st.write("Details at selected index:")
st.write(data.iloc[selected_index])
