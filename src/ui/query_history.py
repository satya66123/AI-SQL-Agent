import streamlit as st

from src.history.query_history import QueryHistory


def show_query_history():

    st.title("📜 Query History")

    history = QueryHistory.get()

    if not history:

        st.info("No query history available.")

        return

    for i, item in enumerate(history, start=1):

        with st.expander(f"{i}. {item['question']}"):

            st.write(f"**Time:** {item['time']}")

            st.write(f"**Database:** {item['database']}")

            st.subheader("Generated Query")

            language = "sql"

            if item["database"] == "MongoDB":

                language = "javascript"

            st.code(

                item["query"],

                language=language

            )

    st.divider()

    if st.button(

        "🗑 Clear History",

        width="stretch"

    ):

        QueryHistory.clear()

        st.success("History cleared.")

        st.rerun()