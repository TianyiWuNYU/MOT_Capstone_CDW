import streamlit as st
import pandas as pd
import csv

st.write("# Data Input")

st.markdown("""
**This page is still under construction, and now we need the dataset files uploaded. More features are coming soon.**
""")

def load_data():
    return pd.read_csv('data/template.csv')

def load_pickup_book():
    return pd.read_csv('data/pickup_address_book.csv')

def load_gene_book():
    return pd.read_csv('data/generator_address_book.csv')

pickup_book = load_pickup_book()
pickup_book['display'] = pickup_book['name'] + ' - ' + pickup_book['address']

generator_book = load_gene_book()
generator_book['display'] = generator_book['name'] + ' - ' + generator_book['address']

def update_pickup(option):
    if option:
        selected_pickup = pickup_book[pickup_book['display'] == option].iloc[0]
        st.session_state.update({
            "pickup_name": selected_pickup['name'],
            "pickup_add": selected_pickup['address'],
            "pickup_city": selected_pickup['city'],
            "pickup_state": selected_pickup['state'],
            "pickup_zip": selected_pickup['zip'],
            "pickup_lat": selected_pickup['lat'],
            "pickup_lng": selected_pickup['lng']
        })

def update_generator(option):
    if option:
        selected_generator = generator_book[generator_book['display'] == option].iloc[0]
        st.session_state.update({
            "gene_name": selected_generator['name'],
            "gene_add": selected_generator['address'],
            "gene_city": selected_generator['city'],
            "gene_state": selected_generator['state'],
            "gene_zip": selected_generator['zip']
        })


pickup_option = st.selectbox('Choose Existing Pickup Location', [''] + pickup_book['display'].tolist(), key='pickup_selection', on_change=update_pickup)
generator_option = st.selectbox('Choose Existing Generator Location', [''] + generator_book['display'].tolist(), key='generator_selection', on_change=update_generator)

with st.form("my_form"):
    st.write("### Pickup Location Details")
    pk_name = st.text_input("Location Name", key="pickup_name")
    pk_add = st.text_input("Address", key="pickup_add")
    pk_city = st.text_input("City", key="pickup_city")
    pk_state = st.text_input("State", key="pickup_state")
    pk_zip = st.text_input("Zip", key="pickup_zip")
    pk_lat = st.text_input("Latitude", key="pickup_lat")
    pk_lng = st.text_input("Longitude", key="pickup_lng")

    st.write("### Generator Location Details")
    gn_name = st.text_input("Location Name", key="gene_name")
    gn_add = st.text_input("Address", key="gene_add")
    gn_city = st.text_input("City", key="gene_city")
    gn_state = st.text_input("State", key="gene_state")
    gn_zip = st.text_input("Zip", key="gene_zip")

    st.write("### Waste Details")
    type_debris = st.text_input("Type of Debris", key="type_debris")
    waste_quantity = st.text_input("Quantity of Waste", key="waste_quantity")
    transporter_name = st.text_input("Transporter Name", key="transporter_name")

    submitted = st.form_submit_button("Submit")

if submitted:
    with open('data/template.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([pk_name, pk_add, pk_city, pk_state, pk_zip, pk_lat, pk_lng, gn_name, gn_add, gn_city, gn_state, gn_zip, type_debris, waste_quantity, transporter_name])
        st.success("Data submitted successfully!")

st.write("### Input Results", load_data())

