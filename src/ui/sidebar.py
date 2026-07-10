import streamlit as st

from src.ui.home import show_home
from src.ui.provider import show_provider
from src.ui.database import show_database
from src.ui.logs import show_logs
from src.ui.settings import show_settings
from src.ui.about import show_about
from src.ui.schema import show_schema
from src.ui.ai_chat import show_ai_chat
from src.ui.dashboard import show_dashboard
from src.ui.saved_queries import show_saved_queries
from src.ui.query_templates import show_query_templates

from src.ui.query_history import show_query_history

from themes import save_theme


def sidebar():

    st.sidebar.title("🤖 AI SQL Agent")

    # Initialize theme
    if "theme" not in st.session_state:
        st.session_state.theme = "Dark"

    theme = st.sidebar.selectbox(
        "🎨 Theme",
        ["Dark", "Light", "Blue"],
        index=["Dark", "Light", "Blue"].index(st.session_state.theme)
    )

    # Change theme
    if theme != st.session_state.theme:
        st.session_state.theme = theme
        save_theme(theme)
        st.rerun()

    menu = st.sidebar.radio(
        "Navigation",
        [
            "🏠 Home",
            "🤖 AI Chat",
            "🤖 AI Provider",
            "📊 Dashboard",
            "🗄 Database",
            "⭐ Saved Queries",
            "📝 Query Templates",
            "📂 Schema Explorer",
            "📜 Query History",
            "📄 Logs",
            "⚙ Settings",
            "ℹ About"
        ]
    )

    pages = {
        "🏠 Home": show_home,
        "🤖 AI Chat": show_ai_chat,
        "🤖 AI Provider": show_provider,
        "📊 Dashboard": show_dashboard,
        "🗄 Database": show_database,
        "⭐ Saved Queries": show_saved_queries,
        "📝 Query Templates": show_query_templates,
        "📜 Query History": show_query_history,
        "📂 Schema Explorer": show_schema,
        "📄 Logs": show_logs,
        "⚙ Settings": show_settings,
        "ℹ About": show_about
    }



    return pages[menu]
