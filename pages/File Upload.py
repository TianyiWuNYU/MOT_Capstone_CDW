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

pickup_book = load_pickup_book()
pickup_book['display'] = pickup_book['name'] + ' - ' + pickup_book['address']

with st.form("my_form"):
    address_option = st.selectbox('Choose Existing Address', [''] + pickup_book['display'].tolist())
    if address_option:
        selected_address = pickup_book[pickup_book['display'] == address_option]
        name = selected_address['name'].iloc[0]
        address = selected_address['address'].iloc[0]
        city = selected_address['city'].iloc[0]
        state = selected_address['state'].iloc[0]
        zip = selected_address['zip'].iloc[0]
    else:
        name = st.text_input("Location Name")
        address = st.text_input("Address")
        city = st.text_input("City")
        state = st.text_input("State")
        zip = st.text_input("Zip")
    submitted = st.form_submit_button("Submit")

if submitted:
    with open('data/test.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([name, address, city, state, zip])
        st.success("Submit Success")

st.write("test dataset", load_test())
