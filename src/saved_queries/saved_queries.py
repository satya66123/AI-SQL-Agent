import streamlit as st


class SavedQueries:

    @staticmethod
    def initialize():

        if "saved_queries" not in st.session_state:

            st.session_state.saved_queries = []

    # ------------------------------------

    @staticmethod
    def save(question, database, query):

        SavedQueries.initialize()

        st.session_state.saved_queries.append(

            {

                "question": question,

                "database": database,

                "query": query

            }

        )

    # ------------------------------------

    @staticmethod
    def get():

        SavedQueries.initialize()

        return st.session_state.saved_queries

    # ------------------------------------

    @staticmethod
    def delete(index):

        SavedQueries.initialize()

        st.session_state.saved_queries.pop(index)