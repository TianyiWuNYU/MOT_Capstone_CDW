import streamlit as st
import pandas as pd
import pydeck as pdk

st.title('DDC Mapping Program')

file_url = 'https://raw.githubusercontent.com/TianyiWuNYU/test/main/data/cdw_csv_processed.csv'
df = pd.read_csv(file_url)

st.write("Data loaded successfully!")

# Helper function to create filter lists with default option
def create_filter_list(column_name):
    return ['All'] + sorted(df[column_name].dropna().unique().tolist())

# Use helper function to dynamically update the lists based on selections
def get_filtered_data():
    debris_filter = create_filter_list('type_debris')
    pickup_filter = create_filter_list('pickup_address')
    receiving_filter = create_filter_list('receiving_address')

    selected_debris = st.selectbox('Select Type of Debris:', debris_filter, index=0)
    if selected_debris != 'All':
        df = df[df['type_debris'] == selected_debris]
        pickup_filter = create_filter_list('pickup_address')
        receiving_filter = create_filter_list('receiving_address')

    selected_pickup_address = st.selectbox('Select Pickup Address:', pickup_filter, index=0)
    if selected_pickup_address != 'All':
        df = df[df['pickup_address'] == selected_pickup_address]
        receiving_filter = create_filter_list('receiving_address')

    selected_receiving_address = st.selectbox('Select Receiving Address:', receiving_filter, index=0)
    if selected_receiving_address != 'All':
        df = df[df['receiving_address'] == selected_receiving_address]

    return df

filtered_data = get_filtered_data()

pickup_color = st.color_picker('Choose a color for pickup addresses', '#FF6347')  
receiving_color = st.color_picker('Choose a color for receiving addresses', '#4682B4')

# Drawing routes function remains as previously defined
def draw_routes(filtered_data, pickup_color, receiving_color):
    # Implement the drawing logic
    pass

draw_routes(filtered_data, pickup_color, receiving_color)
