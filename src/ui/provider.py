import streamlit as st

from src.ai.provider import ProviderManager
from src.ai.model_manager import ModelManager
from config import config

from src.ai.ollama_provider import OllamaProvider
from src.ai.openai_provider import OpenAIProvider
from src.ai.anthropic_provider import AnthropicProvider


def show_provider():

    st.title("🤖 AI Provider")

    providers = [

        "Ollama",

        "OpenAI",

        "Anthropic"

    ]

    provider = st.selectbox(
        "Provider",
        providers
    )




    ProviderManager.set_provider(provider)

    models = ModelManager().get_models(provider)

    if len(models) == 0:

        st.warning("No models found.")

        return

    # Default model from config
    default_model = config.DEFAULT_MODEL

    index = 0
    if default_model in models:
        index = models.index(default_model)

    model = st.selectbox(
        "Model",
        models,
        index=index
    )

    ProviderManager.set_model(model)

    st.success(f"Selected Model: {model}")

    st.divider()

    st.subheader("Provider Status")

    if provider == "Ollama":

        if OllamaProvider().is_running():

            st.success("🟢 Ollama Server Running")

        else:

            st.error("🔴 Ollama Server Offline")

    elif provider == "OpenAI":

        if OpenAIProvider().is_configured():

            st.success("🟢 API Key Configured")

        else:

            st.error("🔴 API Key Missing")

    elif provider == "Anthropic":

        if AnthropicProvider().is_configured():

            st.success("🟢 API Key Configured")

        else:

            st.error("🔴 API Key Missing")