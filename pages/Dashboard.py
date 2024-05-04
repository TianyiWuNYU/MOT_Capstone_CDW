import streamlit as st
import pandas as pd
import pydeck as pdk

st.title('DDC Mapping Program')

# 加载数据
file_url = 'https://raw.githubusercontent.com/TianyiWuNYU/test/main/data/cdw_csv_processed.csv'
df = pd.read_csv(file_url)
st.write("Data loaded successfully!")

# 初始化筛选器的默认选项
default_debris = 'All types of debris'
default_pickup = 'All pickup addresses'
default_receiving = 'All receiving addresses'

# 定义筛选器选择函数
def get_filtered_options(df, selected_debris, selected_pickup_address, selected_receiving_address):
    if selected_debris != default_debris:
        df = df[df['type_debris'] == selected_debris]
    if selected_pickup_address != default_pickup:
        df = df[df['pickup_address'] == selected_pickup_address]
    if selected_receiving_address != default_receiving:
        df = df[df['receiving_address'] == selected_receiving_address]

    debris_options = [default_debris] + sorted(df['type_debris'].unique().tolist())
    pickup_options = [default_pickup] + sorted(df['pickup_address'].unique().tolist())
    receiving_options = [default_receiving] + sorted(df['receiving_address'].unique().tolist())
    return debris_options, pickup_options, receiving_options

# 创建筛选器
selected_debris = st.selectbox('Select Type of Debris:', [default_debris] + sorted(df['type_debris'].unique().tolist()))
selected_pickup_address = st.selectbox('Select Pickup Address:', [default_pickup] + sorted(df['pickup_address'].unique().tolist()))
selected_receiving_address = st.selectbox('Select Receiving Address:', [default_receiving] + sorted(df['receiving_address'].unique().tolist()))

# 依据当前选择更新选项
debris_options, pickup_options, receiving_options = get_filtered_options(df, selected_debris, selected_pickup_address, selected_receiving_address)

# 重新绘制筛选器
selected_debris = st.selectbox('Type of Debris (Updated):', debris_options)
selected_pickup_address = st.selectbox('Pickup Address (Updated):', pickup_options)
selected_receiving_address = st.selectbox('Receiving Address (Updated):', receiving_options)

# 路线颜色选择器
route_color = st.color_picker('Choose a route color', '#87CEEB')

# 筛选并绘制路径
filtered_data = df[
    ((df['type_debris'] == selected_debris) | (selected_debris == default_debris)) &
    ((df['pickup_address'] == selected_pickup_address) | (selected_pickup_address == default_pickup)) &
    ((df['receiving_address'] == selected_receiving_address) | (selected_receiving_address == default_receiving))
]

def draw_routes(filtered_data, route_color):
    if not filtered_data.empty:
        routes = [{
            "from_coordinates": [row['pickup_lng'], row['pickup_lat']],
            "to_coordinates": [row['receiving_lng'], row['receiving_lat']],
            "info": f"Type of Debris: {row['type_debris']}<br>Waste Quantity: {row['waste_quantity']}<br>"
                    f"Pickup Name: {row['pickup_name']}<br>Pickup Address: {row['pickup_address']}<br>"
                    f"Generator Name: {row['generator_name']}<br>Generator Address: {row['generator_address']}"
        } for _, row in filtered_data.iterrows()]

        color = [int(route_color.lstrip('#')[i:i+2], 16) for i in (0, 2, 4)] + [255]  # 将HEX颜色转换为RGBA
        layer = pdk.Layer(
            "ArcLayer", routes,
            get_source_position="from_coordinates",
            get_target_position="to_coordinates",
            get_width=5, get_tilt=15,
            get_source_color=color, get_target_color=color,
            pickable=True, auto_highlight=True)

        view_state = pdk.ViewState(latitude=filtered_data['pickup_lat'].mean(), longitude=filtered_data['pickup_lng'].mean(), zoom=6)
        st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state, tooltip={"html": "<b>Route Information:</b> {info}"}, map_style='mapbox://styles/mapbox/light-v10'))
    else:
        st.error('No routes found for the selected options.')

draw_routes(filtered_data, route_color)

