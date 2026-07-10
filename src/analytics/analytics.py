import streamlit as st


class Analytics:

    @staticmethod
    def initialize():

        if "analytics" not in st.session_state:

            st.session_state.analytics = {

                "total_queries": 0,

                "mysql_queries": 0,

                "mongo_queries": 0,

                "success": 0,

                "failed": 0,

                "execution_times": [],

                "providers": {}

            }

    # ---------------------------------------------

    @staticmethod
    def add(

        database,

        provider,

        execution_time,

        success

    ):

        Analytics.initialize()

        data = st.session_state.analytics

        data["total_queries"] += 1

        if database == "MySQL":

            data["mysql_queries"] += 1

        else:

            data["mongo_queries"] += 1

        if success:

            data["success"] += 1

        else:

            data["failed"] += 1

        data["execution_times"].append(execution_time)

        if provider not in data["providers"]:

            data["providers"][provider] = 0

        data["providers"][provider] += 1

    # ---------------------------------------------

    @staticmethod
    def get():

        Analytics.initialize()

        return st.session_state.analytics