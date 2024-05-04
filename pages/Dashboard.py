import streamlit as st
import pandas as pd
import pydeck as pdk

st.title('DDC Mapping Program')

file_url = 'https://raw.githubusercontent.com/TianyiWuNYU/test/main/data/cdw_csv_processed.csv'
df = pd.read_csv(file_url)

st.write("Data loaded successfully!")

def update_selectors(debris_type, pickup_address, receiving_address):
    if debris_type != 'All types of debris':
        df_filtered = df[df['type_debris'] == debris_type]
    else:
        df_filtered = df

    if pickup_address != 'All pickup addresses':
        df_filtered = df_filtered[df_filtered['pickup_address'] == pickup_address]

    if receiving_address != 'All receiving addresses':
        df_filtered = df_filtered[df_filtered['receiving_address'] == receiving_address]

    return df_filtered

# Initialize session states if not already set
if 'selected_debris' not in st.session_state:
    st.session_state['selected_debris'] = 'All types of debris'
if 'selected_pickup' not in st.session_state:
    st.session_state['selected_pickup'] = 'All pickup addresses'
if 'selected_receiving' not in st.session_state:
    st.session_state['selected_receiving'] = 'All receiving addresses'

# Selector for type of debris
unique_debris_types = ['All types of debris'] + sorted(df['type_debris'].unique())
selected_debris = st.selectbox('Select Type of Debris:', unique_debris_types, index=unique_debris_types.index(st.session_state['selected_debris']))
st.session_state['selected_debris'] = selected_debris

# Update the data based on the selected debris type
df_updated = update_selectors(selected_debris, st.session_state['selected_pickup'], st.session_state['selected_receiving'])

# Selector for pickup address
unique_pickup_addresses = ['All pickup addresses'] + sorted(df_updated['pickup_address'].unique())
selected_pickup_address = st.selectbox('Select Pickup Address:', unique_pickup_addresses, index=unique_pickup_addresses.index(st.session_state['selected_pickup']))
st.session_state['selected_pickup'] = selected_pickup_address

# Update the data based on the selected pickup address
df_updated = update_selectors(selected_debris, selected_pickup_address, st.session_state['selected_receiving'])

# Selector for receiving address
unique_receiving_addresses = ['All receiving addresses'] + sorted(df_updated['receiving_address'].unique())
selected_receiving_address = st.selectbox('Select Receiving Address:', unique_receiving_addresses, index=unique_receiving_addresses.index(st.session_state['selected_receiving']))
st.session_state['selected_receiving'] = selected_receiving_address

# Final update based on all selections
filtered_data = update_selectors(selected_debris, selected_pickup_address, selected_receiving_address)

# Color picker for routes
route_color = st.color_picker('Choose a route color', '#87CEEB')

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

        color = [int(route_color.lstrip('#')[i:i+2], 16) for i in (0, 2, 4)] + [255]  # Convert HEX to RGBA

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

# Drawing routes
draw_routes(filtered_data, route_color)

