import streamlit as st
from datetime import datetime


class QueryHistory:

    @staticmethod
    def initialize():

        if "query_history" not in st.session_state:

            st.session_state["query_history"] = []

    # ----------------------------------------------------

    @staticmethod
    def add(question, database, query):

        QueryHistory.initialize()

        st.session_state["query_history"].insert(

            0,

            {

                "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

                "question": question,

                "database": database,

                "query": query

            }

        )

    # ----------------------------------------------------

    @staticmethod
    def get():

        QueryHistory.initialize()

        return st.session_state["query_history"]

    # ----------------------------------------------------

    @staticmethod
    def clear():

        st.session_state["query_history"] = []