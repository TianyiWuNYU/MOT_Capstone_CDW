import streamlit as st
import pandas as pd
import csv

st.write("# Data Input")

st.markdown(
    """
    **This page is still under construction, and now we need the dataset files uploaded. more features are coming soon.**
    """
)

def load_test():
    return pd.read_csv('data/test.csv')

def load_pickup_book():
    return pd.read_csv('data/pickup_address_book.csv')

if 'selected_name' not in st.session_state:
    st.session_state.selected_name = ""
if 'selected_address' not in st.session_state:
    st.session_state.selected_address = ""
if 'selected_state' not in st.session_state:
    st.session_state.selected_state = ""
if 'selected_city' not in st.session_state:
    st.session_state.selected_city = ""
if 'selected_zip' not in st.session_state:
    st.session_state.selected_zip = ""


pickup_book = load_pickup_book()
pickup_book['display'] = pickup_book['name'] + ' - ' + pickup_book['address']
address_option = st.selectbox('Choose Existing Address', [''] + pickup_book['display'].tolist(), on_change=lambda: update_add_field(address_option))

def update_add_field(selected_option):
    selected_address = pickup_book[pickup_book['display'] == address_option]
    st.session_state.selected_name = selected_address['name'].iloc[0]
    st.session_state.selected_address = selected_address['address'].iloc[0]
    st.session_state.selected_city = selected_address['city'].iloc[0]
    st.session_state.selected_state = selected_address['state'].iloc[0]
    st.session_state.selected_zip = selected_address['zip'].iloc[0]

with st.form("my_form"):
    ln = st.text_input("Location Name", value=st.session_state.selected_name)
    add = st.text_input("Address", value=st.session_state.selected_address)
    ct = st.text_input("City", value=st.session_state.selected_city)
    ste = st.text_input("State", value=st.session_state.selected_state)
    zp = st.text_input("Zip", value=st.session_state.selected_zip)
    if address_option:
        selected_address = pickup_book[pickup_book['display'] == address_option]
        name = selected_address['name'].iloc[0]
        address = selected_address['address'].iloc[0]
        city = selected_address['city'].iloc[0]
        state = selected_address['state'].iloc[0]
        zip = selected_address['zip'].iloc[0]
    else:
        name = ln
        address = add
        city = ct
        state = ste
        zip = zp
    submitted = st.form_submit_button("Submit")

if submitted:
    with open('data/test.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([name, address, city, state, zip])
        st.success("Submit Success")

st.write("test dataset", load_test())
