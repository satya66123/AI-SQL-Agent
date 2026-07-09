import anthropic

from config import config
from src.ai.base_provider import BaseProvider


class AnthropicProvider(BaseProvider):

    def __init__(self):

        self.client = anthropic.Anthropic(

            api_key=config.ANTHROPIC_API_KEY

        )

    def is_configured(self):

        return bool(

            config.ANTHROPIC_API_KEY.strip()

        )

    def list_models(self):

        return [

            "claude-sonnet-4",

            "claude-opus-4"

        ]

    def generate(self, prompt):

        response = self.client.messages.create(

            model="claude-sonnet-4",

            max_tokens=2048,

            messages=[

                {

                    "role": "user",

                    "content": prompt

                }

            ]

        )

        return response.content[0].text