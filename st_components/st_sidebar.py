import streamlit as st
import os


def st_sidebar():
    with st.sidebar:
        md_directory = "docs/"

        md_files = get_markdown_files(md_directory)

        selected_md_file = st.selectbox("Select a Table", md_files)

        if selected_md_file:
            display_markdown_file(os.path.join(md_directory, selected_md_file))


def load_markdown_file(path):
    with open(path, "r", encoding="utf-8") as file:
        return file.read()


def get_markdown_files(directory):
    return [f for f in os.listdir(directory) if f.endswith(".md")]


def display_markdown_file(path):
    md_content = load_markdown_file(path)
    st.markdown(md_content, unsafe_allow_html=True)
