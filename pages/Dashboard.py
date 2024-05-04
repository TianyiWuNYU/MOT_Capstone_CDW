import streamlit as st
import pandas as pd
import pydeck as pdk

st.title('DDC Mapping Program')

# 加载数据
file_url = 'https://raw.githubusercontent.com/TianyiWuNYU/test/main/data/cdw_csv_processed.csv'
df = pd.read_csv(file_url)
st.write("Data loaded successfully!")

# 初始化选择
if 'selected_debris' not in st.session_state:
    st.session_state.selected_debris = 'All types of debris'
if 'selected_pickup_address' not in st.session_state:
    st.session_state.selected_pickup_address = 'All pickup addresses'
if 'selected_receiving_address' not in st.session_state:
    st.session_state.selected_receiving_address = 'All receiving addresses'

# 颜色选择器
pickup_color = st.color_picker('Choose a color for pickup addresses', '#FF6347')
receiving_color = st.color_picker('Choose a color for receiving addresses', '#4682B4')

def update_options():
    """根据当前选择更新其它选项"""
    current_df = df.copy()
    if st.session_state.selected_debris != 'All types of debris':
        current_df = current_df[current_df['type_debris'] == st.session_state.selected_debris]
    if st.session_state.selected_pickup_address != 'All pickup addresses':
        current_df = current_df[current_df['pickup_address'] == st.session_state.selected_pickup_address]
    if st.session_state.selected_receiving_address != 'All receiving addresses':
        current_df = current_df[current_df['receiving_address'] == st.session_state.selected_receiving_address]

    # 确保 debris_types 是一个列表
    debris_types = list(current_df['type_debris'].unique())
    debris_options = ['All types of debris'] + debris_types if debris_types else ['All types of debris']

    pickup_addresses = list(current_df['pickup_address'].unique())
    pickup_options = ['All pickup addresses'] + pickup_addresses if pickup_addresses else ['All pickup addresses']

    receiving_addresses = list(current_df['receiving_address'].unique())
    receiving_options = ['All receiving addresses'] + receiving_addresses if receiving_addresses else ['All receiving_addresses']

    return debris_options, pickup_options, receiving_options

# 获取下拉选项
debris_options, pickup_options, receiving_options = update_options()

# 创建选择器
selected_debris = st.selectbox('Select Type of Debris:', debris_options)
selected_pickup_address = st.selectbox('Select Pickup Address:', pickup_options)
selected_receiving_address = st.selectbox('Select Receiving Address:', receiving_options)

# 更新会话状态
st.session_state.selected_debris = selected_debris
st.session_state.selected_pickup_address = selected_pickup_address
st.session_state.selected_receiving_address = selected_receiving_address

# 过滤数据
filtered_data = df[
    ((df['type_debris'] == selected_debris) | (selected_debris == 'All types of debris')) &
    ((df['pickup_address'] == selected_pickup_address) | (selected_pickup_address == 'All pickup_addresses')) &
    ((df['receiving_address'] == selected_receiving_address) | (selected_receiving_address == 'All receiving_addresses'))
]

# 绘图函数，使用 Pydeck 绘制
def draw_routes(filtered_data, pickup_color, receiving_color):
    st.pydeck_chart(pdk.Deck(
        map_style='mapbox://styles/mapbox/light-v9',
        initial_view_state=pdk.ViewState(
            latitude=37.76,  # 更改为适合你数据的纬度
            longitude=-122.4,  # 更改为适合你数据的经度
            zoom=11,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
               'HexagonLayer',
               data=filtered_data,
               get_position='[longitude, latitude]',
               radius=200,
               elevation_scale=4,
               elevation_range=[0, 1000],
               pickable=True,
               extruded=True,
            ),
        ],
    ))

# 绘制路线图
draw_routes(filtered_data, pickup_color, receiving_color)

