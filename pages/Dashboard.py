import streamlit as st
import pandas as pd
import pydeck as pdk

st.title('DDC Mapping Program')

file_url = 'https://raw.githubusercontent.com/TianyiWuNYU/test/main/data/cdw_csv_processed.csv'
df = pd.read_csv(file_url)

st.write("Data loaded successfully!")

# Initial selection conditions
selected_debris = st.selectbox('Select Type of Debris:', ['All types of debris'] + sorted(df['type_debris'].unique().tolist()))

# Update the data based on the current selections
if selected_debris != 'All types of debris':
    df = df[df['type_debris'] == selected_debris]

selected_pickup_address = st.selectbox('Select Pickup Address:', ['All pickup addresses'] + sorted(df['pickup_address'].unique().tolist()))

if selected_pickup_address != 'All pickup addresses':
    df = df[df['pickup_address'] == selected_pickup_address]

selected_receiving_address = st.selectbox('Select Receiving Address:', ['All receiving addresses'] + sorted(df['receiving_address'].unique().tolist()))

if selected_receiving_address != 'All receiving addresses':
    df = df[df['receiving_address'] == selected_receiving_address]

pickup_color = st.color_picker('Choose a color for pickup addresses', '#FF6347')  
receiving_color = st.color_picker('Choose a color for receiving addresses', '#4682B4')  

filtered_data = df.copy()

def draw_routes(filtered_data, pickup_color, receiving_color):
    # Drawing routes function remains unchanged
    pass

draw_routes(filtered_data, pickup_color, receiving_color)
