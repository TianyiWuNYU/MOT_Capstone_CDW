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

if 'pickup' not in st.session_state:
    st.session_state.pickup = ""
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

pickup_book = load_pickup_book()
pickup_book['display'] = pickup_book['name'] + ' - ' + pickup_book['address']

pickup_option = st.selectbox('Choose Existing Address', [''] + pickup_book['display'].tolist(), on_change=lambda: update_pickup(pickup_option), key="pickup")
test_option = st.selectbox('Choose Existing Address', [''] + pickup_book['display'].tolist(), key="generator")

def update_pickup(option):
    st.session_state.pickup = option
    if option:
        selected_pickup = pickup_book[pickup_book['display'] == option]
        st.session_state.pickup_name = selected_pickup['name'].iloc[0]
        st.session_state.pickup_add = selected_pickup['address'].iloc[0]
        st.session_state.pickup_city = selected_pickup['city'].iloc[0]
        st.session_state.pickup_state = selected_pickup['state'].iloc[0]
        st.session_state.pickup_zip = selected_pickup['zip'].iloc[0]
        st.experimental_rerun()

if pickup_option != st.session_state.pickup:
    update_pickup(pickup_option)

with st.form("my_form"):
    st.write("### Pickup Location")
    name = st.text_input("Location Name", value=st.session_state.pickup_name)
    address = st.text_input("Address", value=st.session_state.pickup_add)
    city = st.text_input("City", value=st.session_state.pickup_city)
    state = st.text_input("State", value=st.session_state.pickup_state)
    zip = st.text_input("Zip", value=st.session_state.pickup_zip)
    submitted = st.form_submit_button("Submit")

if submitted:
    with open('data/test.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([name, address, city, state, zip])
        st.success("Submit Success")

st.write("test dataset", load_test())
