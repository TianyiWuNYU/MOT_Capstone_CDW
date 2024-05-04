import streamlit as st
import pandas as pd
import pydeck as pdk

st.title('DDC Mapping Program')

# 加载数据
file_url = 'https://raw.githubusercontent.com/TianyiWuNYU/test/main/data/cdw_csv_processed.csv'
df = pd.read_csv(file_url)
st.write("Data loaded successfully!")

# 初始化选择状态
if 'selected_debris' not in st.session_state:
    st.session_state['selected_debris'] = 'All types of debris'
if 'selected_pickup_address' not in st.session_state:
    st.session_state['selected_pickup_address'] = 'All pickup addresses'
if 'selected_receiving_address' not in st.session_state:
    st.session_state['selected_receiving_address'] = 'All receiving addresses'

# 筛选数据
def filter_options():
    filtered_data = df[
        ((df['type_debris'] == st.session_state['selected_debris']) | (st.session_state['selected_debris'] == 'All types of debris')) &
        ((df['pickup_address'] == st.session_state['selected_pickup_address']) | (st.session_state['selected_pickup_address'] == 'All pickup addresses')) &
        ((df['receiving_address'] == st.session_state['selected_receiving_address']) | (st.session_state['selected_receiving_address'] == 'All receiving addresses'))
    ]
    debris_options = ['All types of debris'] + sorted(filtered_data['type_debris'].unique())
    pickup_options = ['All pickup addresses'] + sorted(filtered_data['pickup_address'].unique())
    receiving_options = ['All receiving addresses'] + sorted(filtered_data['receiving_address'].unique())
    return debris_options, pickup_options, receiving_options

debris_options, pickup_options, receiving_options = filter_options()

# 用户界面
selected_debris = st.selectbox('Select Type of Debris:', debris_options, index=debris_options.index(st.session_state['selected_debris']), on_change=lambda: st.session_state.update({'selected_debris': selected_debris}))
selected_pickup_address = st.selectbox('Select Pickup Address:', pickup_options, index=pickup_options.index(st.session_state['selected_pickup_address']), on_change=lambda: st.session_state.update({'selected_pickup_address': selected_pickup_address}))
selected_receiving_address = st.selectbox('Select Receiving Address:', receiving_options, index=receiving_options.index(st.session_state['selected_receiving_address']), on_change=lambda: st.session_state.update({'selected_receiving_address': selected_receiving_address}))

# 颜色选择器
pickup_color = st.color_picker('Choose a color for pickup addresses', '#FF6347')
receiving_color = st.color_picker('Choose a color for receiving addresses', '#4682B4')

# 绘制地图
def draw_routes():
    if not df.empty:
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
            for _, row in df.iterrows()
        ]

        layer = pdk.Layer(
            "ArcLayer",
            routes,
            get_source_position="from_coordinates",
            get_target_position="to_coordinates",
            get_width=5,
            get_tilt=15,
            get_source_color=[int(pickup_color.lstrip('#')[i:i+2], 16) for i in (0, 2, 4)] + [255],
            get_target_color=[int(receiving_color.lstrip('#')[i:i+2], 16) for i in (0, 2, 4)] + [255],
            pickable=True,
            auto_highlight=True,
        )

        view_state = pdk.ViewState(
            latitude=df['pickup_lat'].mean(),
            longitude=df['pickup_lng'].mean(),
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

draw_routes()
