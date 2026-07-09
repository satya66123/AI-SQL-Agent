from openai import OpenAI

from config import config
from src.ai.base_provider import BaseProvider


class OpenAIProvider(BaseProvider):

    def __init__(self):

        self.client = OpenAI(

            api_key=config.OPENAI_API_KEY

        )

    def is_configured(self):

        return bool(

            config.OPENAI_API_KEY.strip()

        )

    def list_models(self):

        return [

            "gpt-5.5",

            "gpt-4.1"

        ]

    def generate(self, prompt):

        response = self.client.responses.create(

            model="gpt-5.5",

            input=prompt

        )

        return response.output_text