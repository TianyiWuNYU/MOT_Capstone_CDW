import streamlit as st
import pandas as pd
import csv

st.write("# Data Input")

st.markdown(
    """
    In this section, users can access and interact with the database effortlessly through our user-friendly interface. 
    Users will view data or perform operations. 
    **This page is still under construction, and now we need the dataset files uploaded. more features are coming soon.**
    """
)

def load_test():
    return pd.read_csv('data/test.csv')

def load_pickup_book():
    return pd.read_csv('data/pickup_address_book.csv')

pickup_book = load_address_book()

with st.form("my_form"):
    address_option = st.selectbox('Choose Existing Address', [''] + pickup_book['name'].tolist())
    if address_option:
      selected_address = address_book[address_book['name'] == address_option]
      address = selected_address['address'].iloc[0]
      city = selected_address['city'].iloc[0]
      state = selected_address['state'].iloc[0]
      zip = selected_address['zip'].iloc[0]
    else:
      address = st.text_input("Address")
      city = st.text_input("City")
      state = st.text_input("State")
      zip = st.text_input("Zip")
    
    submitted = st.form_submit_button("submit")
    if submitted:
      with open('test.csv', 'a', newline='', encoding='utf-8') as f:
          writer = csv.writer(f)
          writer.writerow([address, city, state, zip])
      st.success("Submit Success")

st.write("test dataset", load_test())
