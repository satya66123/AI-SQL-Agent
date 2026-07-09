from src.ai.ollama_provider import OllamaProvider
from src.ai.openai_provider import OpenAIProvider
from src.ai.anthropic_provider import AnthropicProvider


class ModelManager:

    def get_models(self, provider):

        if provider == "Ollama":

            return OllamaProvider().list_models()

        if provider == "OpenAI":

            return OpenAIProvider().list_models()

        if provider == "Anthropic":

            return AnthropicProvider().list_models()

        return []