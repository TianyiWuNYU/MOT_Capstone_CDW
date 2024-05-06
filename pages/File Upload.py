import streamlit as st
import pandas as pd
import csv

st.write("# Data Input")

st.markdown(
    "**This page is still under construction, and now we need the dataset files uploaded. More features are coming soon.**"
)

def load_data():
    return pd.read_csv('data/template.csv')

def load_pickup_book():
    return pd.read_csv('data/pickup_address_book.csv')

def load_gene_book():
    return pd.read_csv('data/generator_address_book.csv')

pickup_book = load_pickup_book()
pickup_book['display'] = pickup_book['name'] + ' - ' + pickup_book['address']

gene_book = load_gene_book()  # Ensure to load the correct book for generators
gene_book['display'] = gene_book['name'] + ' - ' + gene_book['address']

with st.form("my_form"):
    pickup_option = st.selectbox('Choose Existing Pickup Location', [''] + pickup_book['display'].tolist(), key="pickup")
    gene_option = st.selectbox('Choose Existing Generator Location', [''] + gene_book['display'].tolist(), key="generator")

    selected_pickup = pickup_book[pickup_book['display'] == pickup_option].iloc[0] if pickup_option else {}
    selected_gene = gene_book[gene_book['display'] == gene_option].iloc[0] if gene_option else {}

    # Inputs for pickup location details
    pk_name = st.text_input("Location Name", value=selected_pickup.get('name', ''), key="pkn")
    pk_add = st.text_input("Address", value=selected_pickup.get('address', ''), key="pka")
    pk_city = st.text_input("City", value=selected_pickup.get('city', ''), key="pkc")
    pk_state = st.text_input("State", value=selected_pickup.get('state', ''), key="pks")
    pk_zip = st.text_input("Zip", value=selected_pickup.get('zip', ''), key="pkz")
    pk_lat = st.text_input("Latitude", value=selected_pickup.get('lat', ''), key="pkt")
    pk_lng = st.text_input("Longitude", value=selected_pickup.get('lng', ''), key="pkg")

    # Inputs for generator location details
    gn_name = st.text_input("Location Name", value=selected_gene.get('name', ''), key="gnn")
    gn_add = st.text_input("Address", value=selected_gene.get('address', ''), key="gna")
    gn_city = st.text_input("City", value=selected_gene.get('city', ''), key="gnc")
    gn_state = st.text_input("State", value=selected_gene.get('state', ''), key="gns")
    gn_zip = st.text_input("Zip", value=selected_gene.get('zip', ''), key="gnz")

    submitted = st.form_submit_button("Submit")

if submitted:
    with open('data/template.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([pk_name, pk_add, pk_city, pk_state, pk_zip, pk_lat, pk_lng, gn_name, gn_add, gn_city, gn_state, gn_zip])
        st.success("Data submitted successfully!")

st.write("### Input Results", load_data())

