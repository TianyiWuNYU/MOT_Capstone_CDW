import streamlit as st

# 下拉框选项和对应的自动填充年龄数据
age_options = {
    "": "",
    "13 years old": "13",
    "14 years old": "14",
    "15 years old": "15"
}

# 初始化或获取当前会话状态中的选项
if 'selected_option' not in st.session_state:
    st.session_state.selected_option = ""

# 创建下拉选择框，不在表单内，以便可以立即响应用户的选择
selected_option = st.selectbox('Choose an age:', list(age_options.keys()), index=list(age_options.keys()).index(st.session_state.selected_option))

# 更新选项
def update_age(option):
    st.session_state.selected_option = option
    # 刷新页面以更新输入框
    st.experimental_rerun()

# 检测选择的改变并更新
if selected_option != st.session_state.selected_option:
    update_age(selected_option)

# 创建表单
with st.form(key='my_form'):
    # 显示一个文本输入框，其内容根据下拉选择自动填充
    age_input = st.text_input('Age:', value=age_options[st.session_state.selected_option])

    # 提交按钮
    submit_button = st.form_submit_button(label='Submit')

# 检查表单是否被提交并处理数据
if submit_button:
    st.write(f'You have selected: {selected_option}, which corresponds to age {age_input}.')
