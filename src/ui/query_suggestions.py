import streamlit as st

from src.suggestions.query_suggestions import QuerySuggestions


def show_suggestions():

    st.subheader("💡 Smart Suggestions")

    suggestions = QuerySuggestions.get()

    cols = st.columns(2)

    for index, suggestion in enumerate(suggestions):

        with cols[index % 2]:

            if st.button(

                suggestion,

                key=f"suggestion_{index}",

                width="stretch"

            ):

                st.session_state["template_question"] = suggestion

                st.rerun()