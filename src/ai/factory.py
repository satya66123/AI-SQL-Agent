from src.ai.provider import ProviderManager

from src.ai.ollama_provider import OllamaProvider
from src.ai.openai_provider import OpenAIProvider
from src.ai.anthropic_provider import AnthropicProvider


class ProviderFactory:

    @staticmethod
    def get_provider():

        provider = ProviderManager.get_provider()

        if provider == "Ollama":

            return OllamaProvider()

        elif provider == "OpenAI":

            return OpenAIProvider()

        elif provider == "Anthropic":

            return AnthropicProvider()

        raise ValueError(
            "Unsupported Provider"
        )