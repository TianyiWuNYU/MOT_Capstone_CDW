import streamlit as st
import pandas as pd
import csv

st.write("# Data Input")

st.markdown(
    """
    **This page is still under construction, and now we need the dataset files uploaded. More features are coming soon.**
    """
)

def load_data():
    return pd.read_csv('data/template.csv')

def load_pickup_book():
    return pd.read_csv('data/pickup_address_book.csv')

def load_gene_book():
    return pd.read_csv('data/generator_address_book.csv')

if 'selected_pickup' not in st.session_state:
    st.session_state.selected_pickup = ""
if 'pickup_name' not in st.session_state:
    st.session_state.pickup_name = ""
if 'pickup_add' not in st.session_state:
    st.session_state.pickup_add = ""
if 'pickup_state' not in st.session_state:
    st.session_state.pickup_state = ""
if 'pickup_city' not in st.session_state:
    st.session_state.pickup_city = ""
if 'pickup_zip' not in st.session_state:
    st.session_state.pickup_zip = ""
if 'pickup_lat' not in st.session_state:
    st.session_state.pickup_lat = ""
if 'pickup_lng' not in st.session_state:
    st.session_state.pickup_lng = ""

if 'selected_gene' not in st.session_state:
    st.session_state.selected_gene = ""
if 'gene_name' not in st.session_state:
    st.session_state.gene_name = ""
if 'gene_add' not in st.session_state:
    st.session_state.gene_add = ""
if 'gene_state' not in st.session_state:
    st.session_state.gene_state = ""
if 'gene_city' not in st.session_state:
    st.session_state.gene_city = ""
if 'gene_zip' not in st.session_state:
    st.session_state.gene_zip = ""

pickup_book = load_pickup_book()
pickup_book['display'] = pickup_book['name'] + ' - ' + pickup_book['address']
gene_book = load_gene_book()
gene_book['display'] = gene_book['name'] + ' - ' + gene_book['address']

pickup_option = st.selectbox('Choose Existing Pickup Location', [''] + pickup_book['display'].tolist())
gene_option = st.selectbox('Choose Existing Generator Location', [''] + gene_book['display'].tolist())

def update_info():
    if pickup_option:
        selected_pickup = pickup_book[pickup_book['display'] == pickup_option].iloc[0]
        st.session_state.update({
            "pickup_name": selected_pickup['name'],
            "pickup_add": selected_pickup['address'],
            "pickup_city": selected_pickup['city'],
            "pickup_state": selected_pickup['state'],
            "pickup_zip": selected_pickup['zip'],
            "pickup_lat": selected_pickup['lat'],
            "pickup_lng": selected_pickup['lng']
        })
    if gene_option:
        selected_gene = gene_book[gene_book['display'] == gene_option].iloc[0]
        st.session_state.update({
            "gene_name": selected_gene['name'],
            "gene_add": selected_gene['address'],
            "gene_city": selected_gene['city'],
            "gene_state": selected_gene['state'],
            "gene_zip": selected_gene['zip']
        })

update_info()

with st.form("my_form"):
    st.write("### Debris Details")
    type_debris = st.text_input("Type of Debris")
    waste_quantity = st.text_input("Quantity of Waste")
    transporter_name = st.text_input("Transporter Name")
    
    st.write("### Pickup Location")
    pk_name = st.text_input("Location Name", value=st.session_state.pickup_name)
    pk_add = st.text_input("Address", value=st.session_state.pickup_add)
    pk_city = st.text_input("City", value=st.session_state.pickup_city)
    pk_state = st.text_input("State", value=st.session_state.pickup_state)
    pk_zip = st.text_input("Zip", value=st.session_state.pickup_zip)
    pk_lat = st.text_input("Latitude", value=st.session_state.pickup_lat)
    pk_lng = st.text_input("Longitude", value=st.session_state.pickup_lng)

    st.write("### Generator Location")
    gn_name = st.text_input("Location Name", value=st.session_state.gene_name)
    gn_add = st.text_input("Address", value=st.session_state.gene_add)
    gn_city = st.text_input("City", value=st.session_state.gene_city)
    gn_state = st.text_input("State", value=st.session_state.gene_state)
    gn_zip = st.text_input("Zip", value=st.session_state.gene_zip)

    submitted = st.form_submit_button("Submit")

if submitted:
    with open('data/template.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([type_debris, waste_quantity, transporter_name, pk_name, pk_add, pk_city, pk_state, pk_zip, pk_lat, pk_lng, gn_name, gn_add, gn_city, gn_state, gn_zip])
        st.success("Submit Success")

st.write("### Input Results", load_data())

