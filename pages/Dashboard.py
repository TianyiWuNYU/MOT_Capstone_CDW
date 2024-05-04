import streamlit as st
import pandas as pd
import pydeck as pdk

st.title('DDC Mapping Program')

# 加载数据
file_url = 'https://raw.githubusercontent.com/TianyiWuNYU/test/main/data/cdw_csv_processed.csv'
df = pd.read_csv(file_url)

# 确保列是字符串类型，以避免比较错误
df['type_debris'] = df['type_debris'].astype(str)
df['pickup_address'] = df['pickup_address'].astype(str)
df['receiving_address'] = df['receiving_address'].astype(str)

st.write("Data loaded successfully!")

def get_filtered_options(df, selected_debris, selected_pickup_address, selected_receiving_address):
    filtered_df = df.copy()
    if selected_debris != 'All types of debris':
        filtered_df = filtered_df[filtered_df['type_debris'] == selected_debris]
    if selected_pickup_address != 'All pickup addresses':
        filtered_df = filtered_df[filtered_df['pickup_address'] == selected_pickup_address]
    if selected_receiving_address != 'All receiving addresses':
        filtered_df = filtered_df[filtered_df['receiving_address'] == selected_receiving_address]

    debris_options = ['All types of debris'] + sorted(filtered_df['type_debris'].unique())
    pickup_options = ['All pickup addresses'] + sorted(filtered_df['pickup_address'].unique())
    receiving_options = ['All receiving addresses'] + sorted(filtered_df['receiving_address'].unique())

    return debris_options, pickup_options, receiving_options

# 初始化选项
selected_debris = st.selectbox('Select Type of Debris:', ['All types of debris'] + sorted(df['type_debris'].unique()))
selected_pickup_address = st.selectbox('Select Pickup Address:', ['All pickup addresses'] + sorted(df['pickup_address'].unique()))
selected_receiving_address = st.selectbox('Select Receiving Address:', ['All receiving addresses'] + sorted(df['receiving_address'].unique()))

# 更新选项
debris_options, pickup_options, receiving_options = get_filtered_options(df, selected_debris, selected_pickup_address, selected_receiving_address)

# 显示更新后的选择器
selected_debris = st.selectbox('Select Type of Debris (Updated):', debris_options)
selected_pickup_address = st.selectbox('Select Pickup Address (Updated):', pickup_options)
selected_receiving_address = st.selectbox('Select Receiving Address (Updated):', receiving_options)

# 显示路径绘制
route_color = st.color_picker('Choose a route color', '#87CEEB')
filtered_data = df[
    ((df['type_debris'] == selected_debris) | (selected_debris == 'All types of debris')) &
    ((df['pickup_address'] == selected_pickup_address) | (selected_pickup_address == 'All pickup addresses')) &
    ((df['receiving_address'] == selected_receiving_address) | (selected_receiving_address == 'All receiving addresses'))
]

