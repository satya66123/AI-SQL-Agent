import streamlit as st

from src.ui.sidebar import sidebar

st.set_page_config(
    page_title="AI SQL Agent",
    page_icon="🤖",
    layout="wide"
)

page = sidebar()

page()