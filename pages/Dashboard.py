import streamlit as st
import pandas as pd
import pydeck as pdk

st.title('DDC Mapping Program')

file_url = 'https://raw.githubusercontent.com/TianyiWuNYU/test/main/data/cdw_csv_processed.csv'
df = pd.read_csv(file_url)

def get_filtered_options(selected_debris, selected_pickup, selected_receiving):
    filtered_df = df.copy()
    if selected_debris != 'All types of debris':
        filtered_df = filtered_df[filtered_df['type_debris'] == selected_debris]
    if selected_pickup != 'All pickup addresses':
        filtered_df = filtered_df[filtered_df['pickup_address'] == selected_pickup]
    if selected_receiving != 'All receiving addresses':
        filtered_df = filtered_df[filtered_df['receiving_address'] == selected_receiving]

    return {
        'debris_options': ['All types of debris'] + sorted(filtered_df['type_debris'].unique()),
        'pickup_options': ['All pickup addresses'] + sorted(filtered_df['pickup_address'].unique()),
        'receiving_options': ['All receiving addresses'] + sorted(filtered_df['receiving_address'].unique()),
    }

# 初始化选择
if 'selected_debris' not in st.session_state:
    st.session_state['selected_debris'] = 'All types of debris'
if 'selected_pickup_address' not in st.session_state:
    st.session_state['selected_pickup_address'] = 'All pickup addresses'
if 'selected_receiving_address' not in st.session_state:
    st.session_state['selected_receiving_address'] = 'All receiving addresses'

# 实时更新选项
options = get_filtered_options(st.session_state['selected_debris'], st.session_state['selected_pickup_address'], st.session_state['selected_receiving_address'])

# 选择框
st.session_state['selected_debris'] = st.selectbox('Select Type of Debris:', options['debris_options'], key='selected_debris')
st.session_state['selected_pickup_address'] = st.selectbox('Select Pickup Address:', options['pickup_options'], key='selected_pickup_address')
st.session_state['selected_receiving_address'] = st.selectbox('Select Receiving Address:', options['receiving_options'], key='selected_receiving_address')

# 绘制地图和其他元素等操作...
st.write("Updates based on selections will appear here.")

