"""
Chat History

Stores conversation history during the
current Streamlit session.
"""

import streamlit as st


class ChatHistory:

    SESSION_KEY = "chat_history"

    @classmethod
    def initialize(cls):

        if cls.SESSION_KEY not in st.session_state:

            st.session_state[cls.SESSION_KEY] = []

    @classmethod
    def add_message(cls, role, content):

        cls.initialize()

        st.session_state[cls.SESSION_KEY].append(

            {

                "role": role,

                "content": content

            }

        )

    @classmethod
    def get_history(cls):

        cls.initialize()

        return st.session_state[cls.SESSION_KEY]

    @classmethod
    def clear_history(cls):

        st.session_state[cls.SESSION_KEY] = []

    @classmethod
    def latest(cls, count=5):

        cls.initialize()

        return st.session_state[cls.SESSION_KEY][-count:]

    @classmethod
    def build_context(cls, count=5):

        cls.initialize()

        history = cls.latest(count)

        context = ""

        for message in history:

            context += (

                f"{message['role'].upper()}:\n"

                f"{message['content']}\n\n"

            )

        return context