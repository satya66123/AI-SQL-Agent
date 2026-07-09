import streamlit as st

from config import config


def show_about():

    st.title("ℹ About")

    st.write(f"Application : {config.APP_NAME}")

    st.write(f"Version : {config.VERSION}")

    st.write("Developed using Streamlit, Python, Ollama, OpenAI and Anthropic.")