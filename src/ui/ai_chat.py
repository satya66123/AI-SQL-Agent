
import streamlit as st
import pandas as pd

from src.agents.orchestrator import AgentOrchestrator

from src.ai.provider import ProviderManager
from src.database.schema_service import SchemaService
from src.ai.model_manager import ModelManager


def show_ai_chat():

    st.title("🤖 AI SQL Assistant")

    st.markdown(
        """
Ask questions in natural language.

Examples:

- Show all employees
- Show employees earning more than 70000
- Show all departments
- Show customers from Hyderabad
"""
    )

    # =====================================================
    # Provider / Model / Database
    # =====================================================

    col1, col2, col3 = st.columns(3)

    with col1:

        provider = st.selectbox(

            "Provider",

            [

                "Ollama",

                "OpenAI",

                "Anthropic"

            ]

        )

        ProviderManager.set_provider(provider)

    with col2:

        models = ModelManager().get_models(provider)

        if models:

            model = st.selectbox(

                "Model",

                models

            )

            ProviderManager.set_model(model)

        else:

            st.warning("No models found.")

            model = ""

    with col3:

        database = st.selectbox(

            "Database",

            [

                "MySQL",

                "MongoDB"

            ]

        )

    if database == "MongoDB":

        schema = SchemaService()

        collections = schema.get_collections()

        collection = st.selectbox(

            "Collection",

            collections

        )

    else:

        collection = ""

    st.divider()

    # =====================================================
    # Question
    # =====================================================

    question = st.text_area(

        "Enter your question",

        placeholder="Example : Show employees earning more than 70000",

        height=120

    )

    # =====================================================
    # Ask AI
    # =====================================================

    if st.button(

        "🚀 Ask AI",

        use_container_width=True

    ):

        if not question.strip():

            st.warning(

                "Please enter a question."

            )

            st.stop()

        with st.spinner(

            "Generating query..."

        ):

            try:

                orchestrator = AgentOrchestrator()

                # -------------------------
                # MySQL
                # -------------------------

                if database == "MySQL":

                    response = orchestrator.process_sql(

                        question

                    )

                # -------------------------
                # MongoDB
                # -------------------------

                else:

                    response = orchestrator.process_mongo(

                        question,

                        collection

                    )

                if not response["success"]:

                    st.error(

                        response["error"]

                    )

                    return

                # -------------------------
                # Generated Query
                # -------------------------

                st.subheader(

                    "Generated Query"

                )

                language = "sql"

                if database == "MongoDB":

                    language = "javascript"

                st.code(

                    response["query"],

                    language=language

                )

                # -------------------------
                # Results
                # -------------------------

                result = response["result"]

                if result["success"]:

                    rows = result.get(

                        "rows",

                        []

                    )

                    if rows:

                        df = pd.DataFrame(

                            rows

                        )

                        st.subheader(

                            "Query Results"

                        )

                        st.dataframe(

                            df,

                            use_container_width=True

                        )

                        st.success(

                            f"{len(df)} row(s) returned."

                        )

                    else:

                        st.info(

                            "Query executed successfully. No rows returned."

                        )

                else:

                    st.error(

                        result["error"]

                    )

                    return

                # -------------------------
                # Explanation
                # -------------------------

                explanation = response.get(

                    "explanation",

                    ""

                )

                if explanation:

                    st.subheader(

                        "AI Explanation"

                    )

                    st.info(

                        explanation

                    )

            except Exception as e:

                st.error(str(e))