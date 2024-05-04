import streamlit as st
import pandas as pd
import pydeck as pdk

st.title('DDC Mapping Program')

file_url = 'https://raw.githubusercontent.com/TianyiWuNYU/test/main/data/cdw_csv_processed.csv'
df = pd.read_csv(file_url)

st.write("Data loaded successfully!")

# 动态更新下拉选项的功能
def update_options(selected_debris, selected_pickup_address, selected_receiving_address):
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

# 默认选项
selected_debris = 'All types of debris'
selected_pickup_address = 'All pickup addresses'
selected_receiving_address = 'All receiving addresses'

debris_options, pickup_options, receiving_options = update_options(selected_debris, selected_pickup_address, selected_receiving_address)

selected_debris = st.selectbox('Select Type of Debris:', debris_options)
selected_pickup_address = st.selectbox('Select Pickup Address:', pickup_options)
selected_receiving_address = st.selectbox('Select Receiving Address:', receiving_options)

# 用户选择颜色
pickup_color = st.color_picker('Choose a color for pickup locations', '#FF6347')
receiving_color = st.color_picker('Choose a color for receiving locations', '#4682B4')

filtered_data = df[
    ((df['type_debris'] == selected_debris) | (selected_debris == 'All types of debris')) &
    ((df['pickup_address'] == selected_pickup_address) | (selected_pickup_address == 'All pickup addresses')) &
    ((df['receiving_address'] == selected_receiving_address) | (selected_receiving_address == 'All receiving addresses'))
]

# 确保筛选逻辑后再次更新选项，以响应可能的变化
_, pickup_options, receiving_options = update_options(selected_debris, selected_pickup_address, selected_receiving_address)

def draw_routes(data):
    if not data.empty:
        # 路径绘制逻辑
        pass  # 使用pydeck绘制逻辑

draw_routes(filtered_data)



