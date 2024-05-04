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

    debris_options = ['All types of debris'] + sorted(current_df['type_debris'].unique().tolist())
    pickup_options = ['All pickup addresses'] + sorted(current_df['pickup_address'].unique().tolist())
    receiving_options = ['All receiving addresses'] + sorted(current_df['receiving_address'].unique().tolist())

    return debris_options, pickup_options, receiving_options

debris_options, pickup_options, receiving_options = update_options()

selected_debris = st.selectbox('Select Type of Debris:', debris_options)
selected_pickup_address = st.selectbox('Select Pickup Address:', pickup_options)
selected_receiving_address = st.selectbox('Select Receiving Address:', receiving_options)

st.session_state.selected_debris = selected_debris
st.session_state.selected_pickup_address = selected_pickup_address
st.session_state.selected_receiving_address = selected_receiving_address

# 过滤数据
filtered_data = df[
    ((df['type_debris'] == selected_debris) | (selected_debris == 'All types of debris')) &
    ((df['pickup_address'] == selected_pickup_address) | (selected_pickup_address == 'All pickup addresses')) &
    ((df['receiving_address'] == selected_receiving_address) | (selected_receiving_address == 'All receiving addresses'))
]

def draw_routes(filtered_data, pickup_color, receiving_color):
    if not filtered_data.empty:
        view_state = pdk.ViewState(
            latitude=filtered_data['latitude'].mean(),  # Adjust this as per your data
            longitude=filtered_data['longitude'].mean(),  # Adjust this as per your data
            zoom=10,
            pitch=50,
        )

        layer = pdk.Layer(
            'LineLayer',
            data=filtered_data,
            get_source_position='[longitude, latitude]',
            get_target_position='[end_longitude, end_latitude]',  # Ensure your data has these fields
            get_color='[200, 30, 0, 160]',
            get_width=5,
        )

        st.pydeck_chart(pdk.Deck(
            initial_view_state=view_state,
            layers=[layer],
            map_style='mapbox://styles/mapbox/light-v9'
        ))

draw_routes(filtered_data, pickup_color, receiving_color)
