"""
Base Agent

Every AI agent inherits from this class.
"""

from abc import ABC, abstractmethod

from src.ai.factory import ProviderFactory


class BaseAgent(ABC):

    def __init__(self):

        # Selected provider
        self.provider = ProviderFactory.get_provider()

    @abstractmethod
    def process(self, question):
        """
        Process the user question.
        """
        pass

    def ask_ai(self, prompt: str):

        """
        Send prompt to selected provider.
        """

        return self.provider.generate(prompt)