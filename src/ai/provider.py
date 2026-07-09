import streamlit as st

from src.ai.model_manager import ModelManager


class ProviderManager:


    @staticmethod
    def set_provider(provider):

        st.session_state["provider"] = provider

    @staticmethod
    def get_provider():

        return st.session_state.get(
            "provider",
            "Ollama"
        )

    @staticmethod
    def set_model(model):

        st.session_state["model"] = model

    @staticmethod
    def get_model():

        return st.session_state.get(
            "model",
            ""
        )