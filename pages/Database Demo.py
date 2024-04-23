import streamlit as st
import pandas as pd

# 从GitHub加载数据
@st.cache
def load_data_from_github(url):
    return pd.read_csv(url)

# GitHub上的CSV文件原始内容URL
github_raw_url = 'https://raw.githubusercontent.com/TianyiWuNYU/test/main/data/cdw_csv_sample.csv'
data = load_data_from_github(github_raw_url)

# 创建一个包含index和generator_name列的小表格
small_table = data[['index', 'generator_name']].copy()

# 展示小表格
st.write("Index 和 Generator Name:")
st.dataframe(small_table)

# 允许用户选择一个index来查看详细信息
selected_index = st.selectbox("Select an index to see details", data['index'])

# 展示用户选中的详细信息
st.write("Details at selected index:")
st.write(data.loc[data['index'] == selected_index])
