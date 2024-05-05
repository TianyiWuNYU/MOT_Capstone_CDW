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
pickup_option = st.selectbox('Choose Existing Pickup Location', [''] + pickup_book['display'].tolist())
generator_book = load_gene_book()
generator_book['display'] = generator_book['name'] + ' - ' + generator_book['address']
generator_option = st.selectbox('Choose Existing Generator Location', [''] + generator_book['display'].tolist())

with st.form("data_entry_form"):
    st.write("### Pickup Location")
    pk_name = st.text_input("Location Name", value="")
    pk_add = st.text_input("Address", value="")
    pk_city = st.text_input("City", value="")
    pk_state = st.text_input("State", value="")
    pk_zip = st.text_input("Zip", value="")
    pk_lat = st.text_input("Latitude", value="")
    pk_lng = st.text_input("Longitude", value="")

    st.write("### Generator Location")
    gn_name = st.text_input("Location Name (Generator)", value="")
    gn_add = st.text_input("Address (Generator)", value="")
    gn_city = st.text_input("City (Generator)", value="")
    gn_state = st.text_input("State (Generator)", value="")
    gn_zip = st.text_input("Zip (Generator)", value="")

    st.write("### Waste Details")
    type_debris = st.text_input("Type of Debris", value="")
    waste_quantity = st.text_input("Waste Quantity", value="")
    transporter_name = st.text_input("Transporter Name", value="")

    submitted = st.form_submit_button("Submit")

if submitted:
    new_data = [pk_name, pk_add, pk_city, pk_state, pk_zip, pk_lat, pk_lng, gn_name, gn_add, gn_city, gn_state, gn_zip, type_debris, waste_quantity, transporter_name]
    with open('data/template.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(new_data)
        st.success("Data submitted successfully!")

st.write("### Input Results", load_data())

