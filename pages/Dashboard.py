import streamlit as st
import pandas as pd
import pydeck as pdk

# 设置页面标题
st.title('DDC Mapping Program')

# 加载数据
file_url = 'https://raw.githubusercontent.com/TianyiWuNYU/test/main/data/cdw_csv_processed.csv'
df = pd.read_csv(file_url)

st.write("Data loaded successfully!")

# 用户界面允许选择type_debris，添加“All types”选项
unique_debris_types = ['All types of debris'] + list(df['type_debris'].unique())
selected_debris = st.selectbox('Select Type of Debris:', unique_debris_types)

# 用户界面允许选择pickup_address，添加“All pickups”选项
unique_pickup_addresses = ['All pickup addresses'] + list(df['pickup_address'].unique())
selected_pickup_address = st.selectbox('Select Pickup Address:', unique_pickup_addresses)

# 用户界面允许选择receiving_address，添加“All receiving addresses”选项
unique_receiving_addresses = ['All receiving addresses'] + list(df['receiving_address'].unique())
selected_receiving_address = st.selectbox('Select Receiving Address:', unique_receiving_addresses)

# 让用户选择颜色
route_color = st.color_picker('Choose a route color', '#87CEEB')  # 默认为天蓝色

# 过滤数据逻辑
filtered_data = df[
    ((df['type_debris'] == selected_debris) | (selected_debris == 'All types of debris')) &
    ((df['pickup_address'] == selected_pickup_address) | (selected_pickup_address == 'All pickup addresses')) &
    ((df['receiving_address'] == selected_receiving_address) | (selected_receiving_address == 'All receiving addresses'))
]

def draw_routes(filtered_data, route_color):
    if not filtered_data.empty:
        routes = [
            {
                "from_coordinates": [row['pickup_lng'], row['pickup_lat']],
                "to_coordinates": [row['receiving_lng'], row['receiving_lat']],
                "info": f"Type of Debris: {row['type_debris']}<br>"
                        f"Waste Quantity: {row['waste_quantity']}<br>"
                        f"Pickup Name: {row['pickup_name']}<br>"
                        f"Pickup Address: {row['pickup_address']}<br>"
                        f"Generator Name: {row['generator_name']}<br>"
                        f"Generator Address: {row['generator_address']}"
            }
            for _, row in filtered_data.iterrows()
        ]

        # 解析用户选择的颜色
        color = [int(route_color.lstrip('#')[i:i+2], 16) for i in (0, 2, 4)] + [255]  # 将HEX颜色转换为RGBA

        layer = pdk.Layer(
            "ArcLayer",
            routes,
            get_source_position="from_coordinates",
            get_target_position="to_coordinates",
            get_width=5,
            get_tilt=15,
            get_color=color,  # 使用用户选择的颜色
            pickable=True,
            auto_highlight=True,
        )

        view_state = pdk.ViewState(
            latitude=filtered_data['pickup_lat'].mean(),
            longitude=filtered_data['pickup_lng'].mean(),
            zoom=6
        )

        st.pydeck_chart(pdk.Deck(
            layers=[layer],
            initial_view_state=view_state,
            tooltip={"html": "<b>Route Information:</b> {info}"},
            map_style='mapbox://styles/mapbox/light-v10'
        ))
    else:
        st.error('No routes found for the selected options.')

# 绘制路线图
draw_routes(filtered_data, route_color)

