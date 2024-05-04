import streamlit as st
import pandas as pd

def run():
    st.set_page_config(page_title="NYU-MOT-CDW", page_icon="👋")
    
    st.write("# Welcome to 2024 CDW Project! 👋")
    st.markdown("""
        ### Project Introduction
        This website, as the final phase of the capstone project, will contain all deliverables of the project and serve as a publicly accessible site for displaying maps.
        
        In this web application, based on the Streamlit framework, the team developed an interactive dashboard to visualize CDW flows in a variety of graphical views. This tool is useful in policy development for CDW recycling and reuse, providing insight into annual flow trends by material type, transaction, and destination, potentially facilitating a more sustainable approach to CDW management.
        ### How to use this web?
    """)

    st.title('About Us')
    team_members = [
        {"name": "Yanfeng Xu", "role": "JIRA", "image_path": "https://raw.githubusercontent.com/TianyiWuNYU/test/main/photo/xu.jpg"},
        {"name": "Tianyi Wu", "role": "Email Communication", "image_path": "https://raw.githubusercontent.com/TianyiWuNYU/test/main/photo/yi.jpg"},
        {"name": "Ruoan Ni", "role": "Meeting Notes", "image_path": "https://raw.githubusercontent.com/TianyiWuNYU/test/main/photo/mao.jpg"},
        {"name": "Rui Xue", "role": "Meeting Moderator", "image_path": "https://raw.githubusercontent.com/TianyiWuNYU/test/main/photo/rui.jpg"}
    ]

    cols = st.columns(4)
    for i, member in enumerate(team_members):
        with cols[i]:
            st.image(member["image_path"], use_column_width=True)
            st.write(member["name"])
            st.write(member["role"])

if __name__ == "__main__":
    run()

