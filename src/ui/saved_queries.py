import streamlit as st

from src.saved_queries.saved_queries import SavedQueries


def show_saved_queries():

    st.title("⭐ Saved Queries")

    queries = SavedQueries.get()

    if not queries:

        st.info("No saved queries.")

        return

    for i, item in enumerate(queries):

        with st.expander(item["question"]):

            st.write("**Database:**", item["database"])

            language = "sql"

            if item["database"] == "MongoDB":

                language = "javascript"

            st.code(

                item["query"],

                language=language

            )

            if st.button(

                "🗑 Delete",

                key=f"delete_{i}",

                width="stretch"

            ):

                SavedQueries.delete(i)

                st.rerun()