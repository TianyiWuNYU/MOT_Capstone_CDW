import streamlit as st
import pandas as pd

# 从GitHub加载数据
@st.cache
def load_data_from_github(url):
    return pd.read_csv(url)

# GitHub上的CSV文件原始内容URL
github_raw_url = 'https://raw.githubusercontent.com/TianyiWuNYU/test/main/data/cdw_csv_sample.csv'
data = load_data_from_github(github_raw_url)

# 选择栏
selected_index = st.selectbox("Select an index", data.index)

# 使用expander来展示详细信息
with st.expander("See details"):
    st.write(data.loc[selected_index])
