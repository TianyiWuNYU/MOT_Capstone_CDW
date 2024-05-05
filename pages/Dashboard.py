import streamlit as st
import pandas as pd
import pydeck as pdk

st.title('DDC Mapping Program')

file_url = 'https://raw.githubusercontent.com/TianyiWuNYU/test/main/data/cdw_csv_processed.csv'
df = pd.read_csv(file_url)
st.write("Data loaded successfully!")

# Ensuring session state keys exist with defaults before use
if 'selected_debris' not in st.session_state:
    st.session_state['selected_debris'] = 'All types of debris'
if 'selected_pickup_address' not in st.session_state:
    st.session_state['selected_pickup_address'] = 'All pickup addresses'
if 'selected_receiving_address' not in st.session_state:
    st.session_state['selected_receiving_address'] = 'All receiving addresses'

selected_debris = st.selectbox('Select Type of Debris:', ['All types of debris'] + sorted(df['type_debris'].unique().tolist()), index=0)
selected_pickup_address = st.selectbox('Select Pickup Address:', ['All pickup addresses'] + sorted(df['pickup_address'].unique().tolist()), index=0)
selected_receiving_address = st.selectbox('Select Receiving Address:', ['All receiving addresses'] + sorted(df['receiving_address'].unique().tolist()), index=0)

pickup_color = st.color_picker('Choose a color for pickup addresses', '#FF6347')  
receiving_color = st.color_picker('Choose a color for receiving addresses', '#4682B4')  

# Apply filters dynamically
filtered_data = df[
    (df['type_debris'] == selected_debris if selected_debris != 'All types of debris' else True) &
    (df['pickup_address'] == selected_pickup_address if selected_pickup_address != 'All pickup addresses' else True) &
    (df['receiving_address'] == selected_receiving_address if selected_receiving_address != 'All receiving addresses' else True)
]

def draw_routes(filtered_data, pickup_color, receiving_color):
    # Ensure there is data to plot
    if not filtered_data.empty:
        # Implementation remains the same
        pass

draw_routes(filtered_data, pickup_color, receiving_color)

