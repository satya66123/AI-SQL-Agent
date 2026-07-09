import streamlit as st
import pandas as pd

from src.database.query_service import QueryService


def show_database():

    st.title("🗄 Database")

    db = st.radio(

        "Database",

        [

            "MySQL",

            "MongoDB"

        ]

    )

    service = QueryService()

    if db == "MySQL":

        sql = st.text_area(

            "SQL Query",

            "SELECT * FROM employees;"
        )

        if st.button("Execute SQL"):

            result = service.execute_sql(sql)

            if result["success"]:

                df = pd.DataFrame(result["rows"])

                st.dataframe(
                    df,
                    use_container_width=True
                )

                st.success(
                    f"Rows Returned : {len(df)}"
                )

            else:

                st.error(result["error"])

    else:

        collection = st.text_input(

            "Collection",

            "employees"

        )

        query = st.text_area(

            "Mongo Query",

            "{}"
        )

        if st.button("Execute Mongo"):

            import json

            result = service.execute_mongo(

                collection,

                json.loads(query)

            )

            if result["success"]:

                df = pd.DataFrame(result["rows"])

                st.dataframe(
                    df,
                    use_container_width=True
                )

                st.success(
                    f"Documents : {len(df)}"
                )

            else:

                st.error(result["error"])