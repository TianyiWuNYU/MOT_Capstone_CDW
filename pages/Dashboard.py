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
    """ 根据当前选择更新其它选项 """
    current_df = df.copy()
    if st.session_state.selected_debris != 'All types of debris':
        current_df = current_df[current_df['type_debris'] == st.session_state.selected_debris]
    if st.session_state.selected_pickup_address != 'All pickup addresses':
        current_df = current_df[current_df['pickup_address'] == st.session_state.selected_pickup_address]
    if st.session_state.selected_receiving_address != 'All receiving addresses':
        current_df = current_df[current_df['receiving_address'] == st.session_state.selected_receiving_address]
    
    debris_options = ['All types of debris'] + sorted(current_df['type_debris'].unique().tolist())
    pickup_options = ['All pickup addresses'] + sorted(current_df['pickup_address'].unique().tolist())
    receiving_options = ['All receiving addresses'] + sorted(current_df['receiving_address'].unique().tolist())

    return debris_options, pickup_options, receiving_options

# 筛选器
debris_options, pickup_options, receiving_options = update_options()

selected_debris = st.selectbox('Select Type of Debris:', debris_options, index=debris_options.index(st.session_state.selected_debris), on_change=update_options)
selected_pickup_address = st.selectbox('Select Pickup Address:', pickup_options, index=pickup_options.index(st.session_state.selected_pickup_address), on_change=update_options)
selected_receiving_address = st.selectbox('Select Receiving Address:', receiving_options, index=receiving_options.index(st.session_state.selected_receiving_address), on_change=update_options)

# 更新会话状态
st.session_state.selected_debris = selected_debris
st.session_state.selected_pickup_address = selected_pickup_address
st.session_state.selected_receiving_address = selected_receiving_address

# 过滤数据
filtered_data = df[
    ((df['type_debris'] == selected_debris) | (selected_debris == 'All types of debris')) &
    ((df['pickup_address'] == selected_pickup_address) | (selected_pickup_address == 'All pickup addresses')) &
    ((df['receiving_address'] == selected_receiving_address) | (selected_receiving_address == 'All receiving addresses'))
]

# 绘图函数，保持不变
def draw_routes(filtered_data, pickup_color, receiving_color):
    # 类似之前的实现
    # ...

# 绘制路线图
draw_routes(filtered_data, pickup_color, receiving_color)

