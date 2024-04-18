import streamlit as st

# 数据字典，模拟下拉选择后对应的自动填充信息
age_options = {
    "Select your option": "",
    "13 years old": "13",
    "14 years old": "14",
    "15 years old": "15"
}

# 初始化或获取当前会话状态
if 'selected_age' not in st.session_state:
    st.session_state.selected_age = ""

# 创建一个表单
with st.form(key='my_form'):
    # 创建下拉选择框
    option = st.selectbox('Choose an option:', list(age_options.keys()), index=0, on_change=lambda: update_age_field(option))

    # 创建年龄输入框，其值取决于下拉框的选择
    age = st.text_input('Age:', value=st.session_state.selected_age)

    # 提交按钮
    submit_button = st.form_submit_button(label='Submit')

def update_age_field(selected_option):
    # 更新会话状态中的年龄字段
    st.session_state.selected_age = age_options[selected_option]

# 检查表单是否被提交并处理数据
if submit_button:
    st.write(f'You have selected: {option}, which corresponds to age {age}.')
