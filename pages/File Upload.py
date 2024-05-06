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
    selected_pickup = pickup_book[pickup_book['display'] == option].iloc[0]
    st.session_state.pickup_name = selected_pickup['name']
    st.session_state.pickup_add = selected_pickup['address']
    st.session_state.pickup_city = selected_pickup['city']
    st.session_state.pickup_state = selected_pickup['state']
    st.session_state.pickup_zip = selected_pickup['zip']
    st.session_state.pickup_lat = selected_pickup['lat']
    st.session_state.pickup_lng = selected_pickup['lng']

def update_generator(option):
    selected_gene = generator_book[generator_book['display'] == option].iloc[0]
    st.session_state.gene_name = selected_gene['name']
    st.session_state.gene_add = selected_gene['address']
    st.session_state.gene_city = selected_gene['city']
    st.session_state.gene_state = selected_gene['state']
    st.session_state.gene_zip = selected_gene['zip']

pickup_option = st.selectbox('Choose Existing Pickup Location', [''] + pickup_book['display'].tolist(), on_change=lambda: update_pickup(st.session_state.pickup_selection), key='pickup_selection')
generator_option = st.selectbox('Choose Existing Generator Location', [''] + generator_book['display'].tolist(), on_change=lambda: update_generator(st.session_state.generator_selection), key='generator_selection')

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

