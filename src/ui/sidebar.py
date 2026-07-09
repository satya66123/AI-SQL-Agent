import streamlit as st

from src.ui.home import show_home
from src.ui.provider import show_provider
from src.ui.database import show_database
from src.ui.logs import show_logs
from src.ui.settings import show_settings
from src.ui.about import show_about
from src.ui.schema import show_schema
from src.ui.ai_chat import show_ai_chat


def sidebar():

    st.sidebar.title("🤖 AI SQL Agent")

    menu = st.sidebar.radio(
        "Navigation",
        [
            "🏠 Home",
            "🤖 AI Chat",
            "🤖 AI Provider",
            "🗄 Database",
            "📂 Schema Explorer",
            "📄 Logs",
            "⚙ Settings",
            "ℹ About"
        ]
    )

    pages = {

        "🏠 Home": show_home,

        "🤖 AI Chat": show_ai_chat,

        "🤖 AI Provider": show_provider,

        "🗄 Database": show_database,

        "📂 Schema Explorer": show_schema,

        "📄 Logs": show_logs,

        "⚙ Settings": show_settings,

        "ℹ About": show_about

    }

    return pages[menu]