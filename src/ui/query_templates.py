import streamlit as st

from src.templates.query_templates import QueryTemplates


def show_query_templates():

    st.title("📝 Query Templates")

    templates = QueryTemplates.get()

    for category, questions in templates.items():

        with st.expander(category):

            for question in questions:

                if st.button(

                    question,

                    key=question,

                    width="stretch"

                ):

                    st.session_state["template_question"] = question

                    st.success("Template selected. Open AI Chat.")