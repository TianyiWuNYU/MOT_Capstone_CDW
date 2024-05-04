import base64
import streamlit as st
from streamlit.logger import get_logger
import pandas as pd


LOGGER = get_logger(__name__)

def load_custom_css():
  css = """
  <style>
        /* Target the grid layout of Streamlit columns directly */
        .st-cd {
            gap: 20px; /* Adjust the gap between columns */
        }
        /* Adjustments for all images in the columns */
        .stImage img {
            width: 100%; /* Makes images responsive within the column width */
        }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

def run():
    st.set_page_config(
        page_title="NYU-MOT-CDW",
        page_icon="👋",
    )

    load_custom_css() 

    st.write("# Welcome to 2024 CDW Project! 👋")

    st.markdown(
        """
        ### Project Introduction
        This website, as the final phase of the capstone project, will contain all deliverables of the project and serve as a publicly accessible site for displaying maps.
        
        In this web application, based on the Streamlit framework, the team developed an interactive dashboard to visualize CDW flows in a variety of graphical views. This tool is useful in policy development for CDW recycling and reuse, providing insight into annual flow trends by material type, transaction, and destination, potentially facilitating a more sustainable approach to CDW management.
        ### How to use this web？    
        """
    )
    st.markdown("""<iframe width="800" height="450" src="https://cdn.pixabay.com/video/2016/12/31/6962-197634410_large.mp4" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>
                """, unsafe_allow_html=True)
    
    
# profile
    st.title('About Us')

# 成员信息列表，包括照片的URL
    team_members = [
        {"name": "Yanfeng Xu", "role": "JIRA", "linkedin": "https://www.linkedin.com/in/yanfeng-xu-734698239/", "email": "yx3104@nyu.edu", "image_path": "/workspaces/test/pic/xu.jpg"},
        {"name": "Tianyi Wu", "role": "Email Communication", "linkedin": "https://www.linkedin.com/in/tianyi-wu-b558a51a3/", "email": "tw2709@nyu.edu", "image_path": "/workspaces/test/pic/yi.jpg"},
        {"name": "Ruoan Ni", "role": "Meeting Notes", "linkedin": "https://www.linkedin.com/in/ruoan-ni-97815424b/", "email": "rn2429@nyu.edu", "image_path": "/workspaces/test/pic/mao.jpg"},
        {"name": "Rui Xue", "role": "Meeting Moderator", "linkedin": "https://www.linkedin.com/in/rui-xue-b854731a4/", "email": "rx2161@nyu.edu", "image_path": "/workspaces/test/pic/rui.jpg"}
]

    st.markdown("""
    ## SPONSORS: Terri C. Matthews
    ### Mentor: Dr. Christopher Policastro
    ### The Team: from MOT at NYU Tandon Class of 2024
    """)
    st.write("")  
    st.write("") 

    cols = st.columns(4)
    for i, member in enumerate(team_members):
        with cols[i]:
            st.image(member["image_path"], use_column_width=True)
            st.write(member["name"])
            st.write(member["role"])
   
# 转换成 DataFrame
    df = pd.DataFrame(team_members)

# 使链接和邮件地址可点击
    def make_clickable(link, text):
        return f'<a target="_blank" href=" ">{text}</a >'

    df['linkedin'] = df.apply(lambda x: make_clickable(x['linkedin'], 'LinkedIn'), axis=1)
    df['email'] = df.apply(lambda x: make_clickable(f"mailto:{x['email']}", x['email']), axis=1)


# 选择要显示的列，调整列顺序
    df = df[['name', 'role', 'email', 'linkedin']]

# 使用 Markdown 显示 DataFrame，并允许 HTML 渲染，以显示图片和链接
    st.title("Connect with us")
    st.write("If you have any problem, please connect with us!")
    st.markdown(df.to_html(escape=False, index=False), unsafe_allow_html=True)


if __name__ == "__main__":
    run()
