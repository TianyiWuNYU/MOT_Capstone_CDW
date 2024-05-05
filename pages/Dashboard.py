import streamlit as st
import pandas as pd
import pydeck as pdk

st.title('DDC Mapping Program')

file_url = 'https://raw.githubusercontent.com/TianyiWuNYU/test/main/data/cdw_csv_processed.csv'
df = pd.read_csv(file_url)
st.write("Data loaded successfully!")

# Ensure correct data types
df['type_debris'] = df['type_debris'].astype(str)
df['pickup_address'] = df['pickup_address'].astype(str)
df['receiving_address'] = df['receiving_address'].astype(str)

# Selection options
type_debris_options = ['All types of debris'] + sorted(df['type_debris'].unique().tolist())
pickup_address_options = ['All pickup addresses'] + sorted(df['pickup_address'].unique().tolist())
receiving_address_options = ['All receiving addresses'] + sorted(df['receiving_address'].unique().tolist())

selected_debris = st.selectbox('Select Type of Debris:', type_debris_options)
selected_pickup_address = st.selectbox('Select Pickup Address:', pickup_address_options)
selected_receiving_address = st.selectbox('Select Receiving Address:', receiving_address_options)

# Filtering data based on selections
filtered_data = df[
    (df['type_debris'] == selected_debris if selected_debris != 'All types of debris' else True) &
    (df['pickup_address'] == selected_pickup_address if selected_pickup_address != 'All pickup addresses' else True) &
    (df['receiving_address'] == selected_receiving_address if selected_receiving_address != 'All receiving addresses' else True)
]

pickup_color = st.color_picker('Choose a color for pickup addresses', '#FF6347')  
receiving_color = st.color_picker('Choose a color for receiving addresses', '#4682B4')  

# Function to draw routes
def draw_routes(filtered_data, pickup_color, receiving_color):
    if not filtered_data.empty:
        # Implementation remains the same
        pass

draw_routes(filtered_data, pickup_color, receiving_color)

