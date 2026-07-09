import streamlit as st

from src.database.schema_service import SchemaService


def show_schema():

    st.title("📂 Schema Explorer")

    database = st.radio(

        "Database",

        [

            "MySQL",

            "MongoDB"

        ]

    )

    schema = SchemaService()

    if database == "MySQL":

        tables = schema.get_tables()

        if not tables:

            st.warning("No tables found.")

            return

        table = st.selectbox(

            "Table",

            tables

        )

        columns = schema.get_columns(table)

        st.dataframe(columns)

    else:

        collections = schema.get_collections()

        collection = st.selectbox(

            "Collection",

            collections

        )

        doc = schema.sample_document(collection)

        st.json(doc)