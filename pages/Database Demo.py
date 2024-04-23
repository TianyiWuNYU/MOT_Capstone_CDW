import streamlit as st
import pandas as pd

# 从GitHub加载数据
@st.cache
def load_data_from_github(url):
    return pd.read_csv(url)

# GitHub上的CSV文件原始内容URL
github_raw_url = 'https://raw.githubusercontent.com/TianyiWuNYU/test/main/data/cdw_csv_sample.csv'
data = load_data_from_github(github_raw_url)

# 打印列名，以便我们可以看到所有可用的列名
st.write("列名：", data.columns.tolist())

# 假设第一列是index，第二列是generator_name，根据您的数据实际情况进行调整
small_table = data.iloc[:, [0, 1]].copy()
small_table.columns = ['index', 'generator_name']  # 重命名列为index和generator_name

# 展示小表格
st.dataframe(small_table)
