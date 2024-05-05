import streamlit as st
import pandas as pd

def load_custom_css():
    css = """
    <style>
        /* Adjust the grid layout of Streamlit columns */
        .st-cd {
            gap: 20px; /* Adjust the gap between columns */
        }
        /* Adjustments for all images in the columns */
        .stImage img {
            width: 100%; /* Makes images responsive within the column width */
            height: 250px; /* Sets a uniform height */
            object-fit: cover; /* Ensures images cover the area well */
        }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

def run():
    st.set_page_config(page_title="NYU-MOT-CDW", page_icon="👋")
    load_custom_css()
    
    st.title('About Us')
    team_members = [
        {"name": "Yanfeng Xu", "role": "JIRA", "image_path": "https://github.com/TianyiWuNYU/test/blob/main/photo/dafd981f824bd141907fffc9e97830b.jpg?raw=true"},
        {"name": "Tianyi Wu", "role": "Email Communication", "image_path": "https://github.com/TianyiWuNYU/test/blob/main/photo/7fdac96ee1bacd291591efe1155f5dd.jpg?raw=true"},
        {"name": "Ruoan Ni", "role": "Meeting Notes", "image_path": "https://github.com/TianyiWuNYU/test/blob/main/photo/8720019c766d7e9d3c85f13aa935398.jpg?raw=true"},
        {"name": "Rui Xue", "role": "Meeting Moderator", "image_path": "https://github.com/TianyiWuNYU/test/blob/main/photo/27d8bbc6a5cd97de219a03a26ec8cb6.jpg?raw=true"}
    ]

    cols = st.columns(4)
    for i, member in enumerate(team_members):
        with cols[i]:
            st.image(member["image_path"], use_column_width=True, output_format='auto')
            st.write(member["name"])
            st.write(member["role"])

if __name__ == "__main__":
    run()

