import streamlit as st
import pandas as pd
import pydeck as pdk

st.title('DDC Mapping Program')

file_url = 'https://raw.githubusercontent.com/TianyiWuNYU/test/main/data/cdw_csv_processed.csv'
df = pd.read_csv(file_url)

st.write("Data loaded successfully!")

def get_filtered_options(df, col, skip_val):
    if skip_val:
        return df[col].unique()
    else:
        return ['All'] + sorted(df[col].unique())

selected_debris = st.selectbox(
    'Select Type of Debris:',
    get_filtered_options(df, 'type_debris', False),
    index=0
)

selected_pickup_address = st.selectbox(
    'Select Pickup Address:',
    get_filtered_options(df[df['type_debris'].isin([selected_debris] if selected_debris != 'All' else df['type_debris'].unique())], 'pickup_address', selected_debris != 'All'),
    index=0
)

selected_receiving_address = st.selectbox(
    'Select Receiving Address:',
    get_filtered_options(df[df['type_debris'].isin([selected_debris] if selected_debris != 'All' else df['type_debris'].unique()) & df['pickup_address'].isin([selected_pickup_address] if selected_pickup_address != 'All' else df['pickup_address'].unique())], 'receiving_address', selected_debris != 'All' or selected_pickup_address != 'All'),
    index=0
)

route_color = st.color_picker('Choose a route color', '#0000FF')

filtered_data = df[
    ((df['type_debris'] == selected_debris) | (selected_debris == 'All')) &
    ((df['pickup_address'] == selected_pickup_address) | (selected_pickup_address == 'All')) &
    ((df['receiving_address'] == selected_receiving_address) | (selected_receiving_address == 'All'))
]

def draw_routes(data, color):
    if not data.empty:
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
            for _, row in data.iterrows()
        ]

        color = [int(color.lstrip('#')[i:i+2], 16) for i in (0, 2, 4)] + [255]  # 将HEX颜色转换为RGBA

        layer = pdk.Layer(
            "ArcLayer",
            routes,
            get_source_position="from_coordinates",
            get_target_position="to_coordinates",
            get_width=5,
            get_tilt=15,
            get_color=color,
            pickable=True,
            auto_highlight=True,
        )

        view_state = pdk.ViewState(
            latitude=data['pickup_lat'].mean(),
            longitude=data['pickup_lng'].mean(),
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

draw_routes(filtered_data, route_color)



