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

pickup_book = load_pickup_book()
pickup_book['display'] = pickup_book['name'] + ' - ' + pickup_book['address']
generator_book = load_gene_book()
generator_book['display'] = generator_book['name'] + ' - ' + generator_book['address']

def update_pickup_details():
    if st.session_state['pickup_selection']:
        selected = pickup_book[pickup_book['display'] == st.session_state['pickup_selection']].iloc[0]
        st.session_state['pk_name'] = selected['name']
        st.session_state['pk_add'] = selected['address']
        st.session_state['pk_city'] = selected['city']
        st.session_state['pk_state'] = selected['state']
        st.session_state['pk_zip'] = selected['zip']
        st.session_state['pk_lat'] = selected['lat']
        st.session_state['pk_lng'] = selected['lng']

def update_generator_details():
    if st.session_state['generator_selection']:
        selected = generator_book[generator_book['display'] == st.session_state['generator_selection']].iloc[0]
        st.session_state['gn_name'] = selected['name']
        st.session_state['gn_add'] = selected['address']
        st.session_state['gn_city'] = selected['city']
        st.session_state['gn_state'] = selected['state']
        st.session_state['gn_zip'] = selected['zip']

st.selectbox('Choose Existing Pickup Location', [''] + pickup_book['display'].tolist(), key='pickup_selection', on_change=update_pickup_details)
st.selectbox('Choose Existing Generator Location', [''] + generator_book['display'].tolist(), key='generator_selection', on_change=update_generator_details)

with st.form("data_entry_form"):
    st.write("### Pickup Location")
    pk_name = st.text_input("Location Name", key="pk_name")
    pk_add = st.text_input("Address", key="pk_add")
    pk_city = st.text_input("City", key="pk_city")
    pk_state = st.text_input("State", key="pk_state")
    pk_zip = st.text_input("Zip", key="pk_zip")
    pk_lat = st.text_input("Latitude", key="pk_lat")
    pk_lng = st.text_input("Longitude", key="pk_lng")

    st.write("### Generator Location")
    gn_name = st.text_input("Location Name (Generator)", key="gn_name")
    gn_add = st.text_input("Address (Generator)", key="gn_add")
    gn_city = st.text_input("City (Generator)", key="gn_city")
    gn_state = st.text_input("State (Generator)", key="gn_state")
    gn_zip = st.text_input("Zip (Generator)", key="gn_zip")

    submitted = st.form_submit_button("Submit")

if submitted:
    new_data = [pk_name, pk_add, pk_city, pk_state, pk_zip, pk_lat, pk_lng, gn_name, gn_add, gn_city, gn_state, gn_zip]
    with open('data/template.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(new_data)
        st.success("Data submitted successfully!")

st.write("### Input Results", load_data())

