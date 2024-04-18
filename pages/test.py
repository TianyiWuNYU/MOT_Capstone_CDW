import streamlit as st
import pandas as pd
import csv

st.title("Data Input")
st.markdown("**This page is still under construction. More features are coming soon.**")

# Load data functions
def load_test():
    return pd.read_csv('data/test.csv')

def load_pickup_book():
    try:
        data = pd.read_csv('data/pickup_address_book.csv')
        data['display'] = data['name'] + ' - ' + data['address']
        return data
    except FileNotFoundError:
        return pd.DataFrame(columns=['name', 'address', 'city', 'state', 'zip', 'display'])

# Load address book and manage session state
pickup_book = load_pickup_book()
if 'selected_display' not in st.session_state:
    st.session_state['selected_display'] = ""

# Update function for dropdown
def update_address_fields(option):
    if option:
        selected_data = pickup_book[pickup_book['display'] == option].iloc[0]
        st.session_state['selected_name'] = selected_data['name']
        st.session_state['selected_address'] = selected_data['address']
        st.session_state['selected_city'] = selected_data['city']
        st.session_state['selected_state'] = selected_data['state']
        st.session_state['selected_zip'] = selected_data['zip']

# Address dropdown selector
address_option = st.selectbox('Choose Existing Address', [''] + pickup_book['display'].tolist(), index=pickup_book['display'].tolist().index(st.session_state['selected_display']) if st.session_state['selected_display'] in pickup_book['display'].tolist() else 0)
if address_option != st.session_state['selected_display']:
    st.session_state['selected_display'] = address_option
    update_address_fields(address_option)

# Form for data input
with st.form("my_form"):
    name = st.text_input("Location Name", value=st.session_state.get('selected_name', ''))
    address = st.text_input("Address", value=st.session_state.get('selected_address', ''))
    city = st.text_input("City", value=st.session_state.get('selected_city', ''))
    state = st.text_input("State", value=st.session_state.get('selected_state', ''))
    zip_code = st.text_input("Zip", value=st.session_state.get('selected_zip', ''))
    submitted = st.form_submit_button("Submit")

    if submitted:
        with open('data/test.csv', 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([name, address, city, state, zip_code])
            st.success("Data submitted successfully!")

# Display updated dataset
st.write("Updated dataset:", load_test())
