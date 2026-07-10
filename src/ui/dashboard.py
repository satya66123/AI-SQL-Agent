import streamlit as st

from src.analytics.analytics import Analytics


def show_dashboard():

    st.title("📊 Dashboard Analytics")

    data = Analytics.get()

    col1, col2, col3 = st.columns(3)

    col1.metric(

        "Total Queries",

        data["total_queries"]

    )

    col2.metric(

        "MySQL",

        data["mysql_queries"]

    )

    col3.metric(

        "MongoDB",

        data["mongo_queries"]

    )

    st.divider()

    col4, col5 = st.columns(2)

    col4.metric(

        "Successful",

        data["success"]

    )

    col5.metric(

        "Failed",

        data["failed"]

    )

    st.divider()

    if data["execution_times"]:

        avg = sum(

            data["execution_times"]

        ) / len(

            data["execution_times"]

        )

    else:

        avg = 0

    st.metric(

        "Average Execution Time",

        f"{avg:.3f} sec"

    )

    st.divider()

    st.subheader("Provider Usage")

    st.bar_chart(

        data["providers"],

        width="stretch"

    )