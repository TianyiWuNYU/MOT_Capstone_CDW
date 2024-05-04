import streamlit as st
import pandas as pd
import pydeck as pdk

st.title('DDC Mapping Program')

# 加载数据
file_url = 'https://raw.githubusercontent.com/TianyiWuNYU/test/main/data/cdw_csv_processed.csv'
df = pd.read_csv(file_url)
st.write("Data loaded successfully!")

# 初始化session_state，如果没有初始化过
if 'selected_debris' not in st.session_state:
    st.session_state['selected_debris'] = 'All types of debris'
if 'selected_pickup' not in st.session_state:
    st.session_state['selected_pickup'] = 'All pickup addresses'
if 'selected_receiving' not in st.session_state:
    st.session_state['selected_receiving'] = 'All receiving addresses'

# 用来根据选择更新选项的函数
def update_options():
    debris_mask = (df['type_debris'] == st.session_state['selected_debris']) | (st.session_state['selected_debris'] == 'All types of debris')
    pickup_mask = (df['pickup_address'] == st.session_state['selected_pickup']) | (st.session_state['selected_pickup'] == 'All pickup addresses')
    receiving_mask = (df['receiving_address'] == st.session_state['selected_receiving']) | (st.session_state['selected_receiving'] == 'All receiving addresses')
    filtered_df = df[debris_mask & pickup_mask & receiving_mask]
    
    unique_debris_types = ['All types of debris'] + sorted(filtered_df['type_debris'].unique().tolist())
    unique_pickup_addresses = ['All pickup addresses'] + sorted(filtered_df['pickup_address'].unique().tolist())
    unique_receiving_addresses = ['All receiving addresses'] + sorted(filtered_df['receiving_address'].unique().tolist())
    
    return unique_debris_types, unique_pickup_addresses, unique_receiving_addresses

# 选择过滤器
def on_change():
    st.session_state['update'] = True

selected_debris = st.selectbox('Select Type of Debris:', update_options()[0], on_change=on_change, key='selected_debris')
selected_pickup_address = st.selectbox('Select Pickup Address:', update_options()[1], on_change=on_change, key='selected_pickup')
selected_receiving_address = st.selectbox('Select Receiving Address:', update_options()[2], on_change=on_change, key='selected_receiving')

pickup_color = st.color_picker('Choose a color for pickup addresses', '#FF6347')  
receiving_color = st.color_picker('Choose a color for receiving addresses', '#4682B4')  

filtered_data = df[
    ((df['type_debris'] == selected_debris) | (selected_debris == 'All types of debris')) &
    ((df['pickup_address'] == selected_pickup_address) | (selected_pickup_address == 'All pickup addresses')) &
    ((df['receiving_address'] == selected_receiving_address) | (selected_receiving_address == 'All receiving addresses'))
]

# 绘制路径的函数
def draw_routes(filtered_data, pickup_color, receiving_color):
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

        pickup_color_rgba = [int(pickup_color.lstrip('#')[i:i+2], 16) for i in (0, 2, 4)] + [255]
        receiving_color_rgba = [int(receiving_color.lstrip('#')[i:i+2], 16) for i in (0, 2, 4)] + [255]

        layer = pdk.Layer(
            "ArcLayer",
            routes,
            get_source_position="from_coordinates",
            get_target_position="to_coordinates",
            get_width=5,
            get_tilt=15,
            get_source_color=pickup_color_rgba,
            get_target_color=receiving_color_rgba,
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

draw_routes(filtered_data, pickup_color, receiving_color)


