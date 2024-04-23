import streamlit as st
import pandas as pd

@st.cache
def load_data_from_github(url):
    return pd.read_csv(url)

github_raw_url = 'https://raw.githubusercontent.com/TianyiWuNYU/test/main/data/cdw_csv_sample.csv'
data = load_data_from_github(github_raw_url)

# 假设 DataFrame 的第二列是 generator_name，这里根据您实际的列索引调整
small_table = data[['generator_name']].copy()
small_table.reset_index(inplace=True)  # 将索引列添加为 DataFrame 的列

st.write("小表格显示 `index` 和 `generator_name`：")
st.dataframe(small_table)

# 允许用户选择一个 index 来查看详细信息
selected_index = st.selectbox("Select an index to see details", small_table['index'])

# 展示用户选中的详细信息
st.write("Details at selected index:")
st.write(data.iloc[selected_index])
