import requests
import ollama

from config import config
from src.ai.base_provider import BaseProvider


class OllamaProvider(BaseProvider):

    def list_models(self):

        try:

            response = requests.get(
                f"{config.OLLAMA_HOST}/api/tags",
                timeout=10
            )

            data = response.json()

            models = []

            for model in data.get("models", []):

                name = model["name"].lower()

                if "embed" in name:
                    continue

                if "cloud" in name:
                    continue

                models.append(model["name"])

            return sorted(set(models))

        except Exception:

            return []

    def is_running(self):

        try:

            response = requests.get(
                f"{config.OLLAMA_HOST}/api/tags",
                timeout=5
            )

            return response.status_code == 200

        except Exception:

            return False

    def generate(self, prompt):

        response = ollama.chat(

            model=config.DEFAULT_MODEL,

            messages=[

                {

                    "role": "user",

                    "content": prompt

                }

            ]

        )

        return response["message"]["content"]