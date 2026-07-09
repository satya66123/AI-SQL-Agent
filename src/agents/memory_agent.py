from src.history.chat_history import ChatHistory


class MemoryAgent:

    def __init__(self, history_limit=5):

        self.history_limit = history_limit

    def get_context(self):

        return ChatHistory.build_context(
            self.history_limit
        )

    def build_prompt(self, question):

        context = self.get_context()

        if context.strip():

            return f"""
Previous Conversation

{context}

Current User Question

{question}
"""

        return question

    def save_user_message(self, message):

        ChatHistory.add_message(
            "user",
            message
        )

    def save_assistant_message(self, message):

        ChatHistory.add_message(
            "assistant",
            message
        )

    def clear(self):

        ChatHistory.clear_history()