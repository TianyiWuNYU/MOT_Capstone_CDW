import streamlit as st

# 下拉框选项和对应的自动填充年龄数据
age_options = {
    "": "",
    "13 years old": "13",
    "14 years old": "14",
    "15 years old": "15"
}

# 使用 Streamlit 的状态管理来保存选中的选项
if 'selected_age' not in st.session_state:
    st.session_state['selected_age'] = ""

# 创建下拉选择框，不在表单内，以便可以立即响应用户的选择
selected_option = st.selectbox('Choose an age:', list(age_options.keys()), on_change=lambda: update_age(selected_option))

# 更新年龄输入框的函数
def update_age(option):
    st.session_state['selected_age'] = age_options[option]

# 创建表单
with st.form(key='my_form'):
    # 显示一个文本输入框，其内容根据下拉选择自动填充
    age_input = st.text_input('Age:', value=st.session_state['selected_age'])

    # 提交按钮
    submit_button = st.form_submit_button(label='Submit')

# 检查表单是否被提交并处理数据
if submit_button:
    st.write(f'You have selected: {selected_option}, which corresponds to age {age_input}.')
