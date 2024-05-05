import streamlit as st
import pandas as pd

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
    st.set_page_config(page_title="NYU-MOT-CDW", page_icon="👋")
    load_custom_css()
    
    st.write("# Welcome to 2024 CDW Project! 👋")
    st.markdown("""
        ### Project Introduction
        This website, as the final phase of the capstone project, will contain all deliverables of the project and serve as a publicly accessible site for displaying maps.
        
        In this web application, based on the Streamlit framework, the team developed an interactive dashboard to visualize CDW flows in a variety of graphical views. This tool is useful in policy development for CDW recycling and reuse, providing insight into annual flow trends by material type, transaction, and destination, potentially facilitating a more sustainable approach to CDW management.
        ### How to use this web?    
        """)
    
    st.markdown("""<iframe width="800" height="450" src="https://cdn.pixabay.com/video/2016/12/31/6962-197634410_large.mp4" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>
                """, unsafe_allow_html=True)
    
    # Profile section
    st.title('About Us')
    team_members = [
        {"name": "Yanfeng Xu", "role": "JIRA", "linkedin": "https://www.linkedin.com/in/yanfeng-xu-734698239/", "email": "yx3104@nyu.edu", "image_path": "https://github.com/TianyiWuNYU/test/blob/main/photo/dafd981f824bd141907fffc9e97830b.jpg?raw=true"},
        {"name": "Tianyi Wu", "role": "Email Communication", "linkedin": "https://www.linkedin.com/in/tianyi-wu-b558a51a3/", "email": "tw2709@nyu.edu", "image_path": "https://github.com/TianyiWuNYU/test/blob/main/photo/7fdac96ee1bacd291591efe1155f5dd.jpg?raw=true"},
        {"name": "Ruoan Ni", "role": "Meeting Notes", "linkedin": "https://www.linkedin.com/in/ruoan-ni-97815424b/", "email": "rn2429@nyu.edu", "image_path": "https://github.com/TianyiWuNYU/test/blob/main/photo/8720019c766d7e9d3c85f13aa935398.jpg?raw=true"},
        {"name": "Rui Xue", "role": "Meeting Moderator", "linkedin": "https://www.linkedin.com/in/rui-xue-b854731a4/", "email": "rx2161@nyu.edu", "image_path": "https://github.com/TianyiWuNYU/test/blob/main/photo/27d8bbc6a5cd97de219a03a26ec8cb6.jpg?raw=true"}
    ]

    cols = st.columns(4)
    for i, member in enumerate(team_members):
        with cols[i]:
            st.image(member["image_path"], use_column_width=True)
            st.write(member["name"])
            st.write(member["role"])
    
    # Convert to DataFrame
    df = pd.DataFrame(team_members)
    # Making links clickable
    def make_clickable(link, text):
        return f'<a target="_blank" href="{link}">{text}</a>'

    df['linkedin'] = df.apply(lambda x: make_clickable(x['linkedin'], 'LinkedIn'), axis=1)
    df['email'] = df.apply(lambda x: make_clickable(f"mailto:{x['email']}", x['email']), axis=1)
    
    # Selecting columns and adjusting the order
    df = df[['name', 'role', 'email', 'linkedin']]

    # Displaying the DataFrame using Markdown with HTML rendering to show links
    st.title("Connect with us")
    st.write("If you have any problem, please connect with us!")
    st.markdown(df.to_html(escape=False, index=False), unsafe_allow_html=True)

if __name__ == "__main__":
    run()

