import streamlit as st
import pandas as pd

def load_data_from_github(url):
    return pd.read_csv(url)

github_raw_url = 'https://raw.githubusercontent.com/TianyiWuNYU/test/main/data/cdw_csv_sample.csv'

data = load_data_from_github(github_raw_url)

if len(data.columns) > 1:
    third_column_data = data.iloc[:, 1].to_frame()
    third_column_data['index'] = third_column_data.index
    st.dataframe(third_column_data)
    
    selected_indices = st.multiselect("Select an index", third_column_data['index'])
    for selected_index in selected_indices:
        st.write(data.loc[selected_index, :])

    st.write(data)

