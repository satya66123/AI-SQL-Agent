import streamlit as st
import pandas as pd

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

    provider_df = pd.DataFrame(

        {

            "Provider": list(data["providers"].keys()),

            "Queries": list(data["providers"].values())

        }

    )

    if not provider_df.empty:
        provider_df = provider_df.set_index("Provider")

        st.bar_chart(

            provider_df,

            width="stretch"

        )

    st.divider()

    st.subheader("Database Usage")

    database_df = pd.DataFrame(

        {

            "Database": [

                "MySQL",

                "MongoDB"

            ],

            "Queries": [

                data["mysql_queries"],

                data["mongo_queries"]

            ]

        }

    )

    database_df = database_df.set_index("Database")

    st.bar_chart(

        database_df,

        width="stretch"

    )

    st.divider()

    st.subheader("Success vs Failed")

    status_df = pd.DataFrame(

        {

            "Status": [

                "Success",

                "Failed"

            ],

            "Count": [

                data["success"],

                data["failed"]

            ]

        }

    )

    status_df = status_df.set_index("Status")

    st.bar_chart(

        status_df,

        width="stretch"

    )