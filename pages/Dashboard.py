import streamlit as st
import pandas as pd
import pydeck as pdk

st.title('DDC Mapping Program')

# 加载数据
file_url = 'https://raw.githubusercontent.com/TianyiWuNYU/test/main/data/cdw_csv_processed.csv'
df = pd.read_csv(file_url)

# 确保所有相关列均为字符串类型，以避免类型错误
df['type_debris'] = df['type_debris'].astype(str)
df['pickup_address'] = df['pickup_address'].astype(str)
df['receiving_address'] = df['receiving_address'].astype(str)

# 初始化选择状态
if 'selected_debris' not in st.session_state:
    st.session_state['selected_debris'] = 'All types of debris'
if 'selected_pickup_address' not in st.session_state:
    st.session_state['selected_pickup_address'] = 'All pickup addresses'
if 'selected_receiving_address' not in st.session_state:
    st.session_state['selected_receiving_address'] = 'All receiving addresses'

def get_options():
    # 根据当前选项过滤DataFrame
    debris_filter = (df['type_debris'] == st.session_state['selected_debris']) | (st.session_state['selected_debris'] == 'All types of debris')
    pickup_filter = (df['pickup_address'] == st.session_state['selected_pickup_address']) | (st.session_state['selected_pickup_address'] == 'All pickup addresses')
    receiving_filter = (df['receiving_address'] == st.session_state['selected_receiving_address']) | (st.session_state['selected_receiving_address'] == 'All receiving addresses')
    
    filtered_df = df[debris_filter & pickup_filter & receiving_filter]

    # 生成选项列表
    debris_options = ['All types of debris'] + sorted(filtered_df['type_debris'].unique())
    pickup_options = ['All pickup addresses'] + sorted(filtered_df['pickup_address'].unique())
    receiving_options = ['All receiving addresses'] + sorted(filtered_df['receiving_address'].unique())
    
    return debris_options, pickup_options, receiving_options

# 实时更新选项
debris_options, pickup_options, receiving_options = get_options()

# 选择框与session state连接
st.session_state['selected_debris'] = st.selectbox('Select Type of Debris:', debris_options, key='selected_debris')
st.session_state['selected_pickup_address'] = st.selectbox('Select Pickup Address:', pickup_options, key='selected_pickup_address')
st.session_state['selected_receiving_address'] = st.selectbox('Select Receiving Address:', receiving_options, key='selected_receiving_address')

# 根据选择重新计算选项
debris_options, pickup_options, receiving_options = get_options()

# 绘制地图和其他元素等操作...
# 确保这部分操作使用的是最新的 filtered_df

st.write("Updates based on selections will appear here.")


