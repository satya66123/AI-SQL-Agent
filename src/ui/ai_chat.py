from src.utils.query_formatter import QueryFormatter
import streamlit as st
import pandas as pd
import io
from src.ui.query_suggestions import show_suggestions

from src.utils.pdf_export import PDFExport

from src.analytics.analytics import Analytics

from src.agents.orchestrator import AgentOrchestrator

from src.ai.provider import ProviderManager
from src.database.schema_service import SchemaService
from src.ai.model_manager import ModelManager
from src.history.query_history import QueryHistory
from src.utils.execution_metrics import ExecutionMetrics
from src.utils.chart_generator import ChartGenerator
from src.saved_queries.saved_queries import SavedQueries


def show_ai_chat():

    st.title("🤖 AI SQL Assistant")

    show_suggestions()

    st.divider()


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

    default_question = ""

    if "template_question" in st.session_state:
        default_question = st.session_state["template_question"]

    question = st.text_area(

        "Enter your question",

        value=default_question,

        placeholder="Example : Show employees earning more than 70000",

        height=120

    )

    # =====================================================
    # Ask AI
    # =====================================================

    if st.button(
        "🚀 Ask AI",
        width="stretch"
    ):

        if not question.strip():

            st.warning("Please enter a question.")
            st.stop()

        with st.spinner("Generating query..."):

            metrics = ExecutionMetrics()
            metrics.start()

            try:

                orchestrator = AgentOrchestrator()

                if database == "MySQL":

                    response = orchestrator.process_sql(question)

                else:

                    response = orchestrator.process_mongo(
                        question,
                        collection
                    )

                metrics.stop()

                Analytics.add(

                    database,

                    provider,

                    metrics.elapsed(),

                    response["success"]

                )

                if not response["success"]:

                    st.error(response["error"])
                    return

                QueryHistory.add(
                    question,
                    database,
                    response["query"]
                )

                SavedQueries.save(

                    question,

                    database,

                    response["query"]

                )

                st.success("Query saved automatically.")
                print("Query saved automatically.")


                # =====================================================
                # Generated Query
                # =====================================================

                st.subheader("Generated Query")

                language = "sql"

                if database == "MongoDB":
                    language = "javascript"

                if database == "MySQL":

                    formatted_query = QueryFormatter.format_sql(
                        response["query"]
                    )

                else:

                    formatted_query = response["query"]

                st.code(
                    formatted_query,
                    language=language
                )



                # =====================================================
                # Results
                # =====================================================

                result = response["result"]

                documents = result.get("rows", [])

                row_count = len(documents)

                if result["success"]:

                    if row_count > 0:

                        df = pd.DataFrame(documents)

                        st.subheader("Query Results")

                        st.dataframe(
                            df,
                            width="stretch"
                        )

                        st.success(
                            f"{row_count} row(s) returned."
                        )

                        ChartGenerator.show(df)
                        # =====================================================
                        # Export Results
                        # =====================================================

                        st.divider()

                        st.subheader("📥 Export Results")

                        col_csv, col_excel = st.columns(2)

                        # -------------------------
                        # CSV
                        # -------------------------

                        csv = df.to_csv(index=False).encode("utf-8")

                        with col_csv:

                            st.download_button(

                                label="📄 Download CSV",

                                data=csv,

                                file_name="query_results.csv",

                                mime="text/csv",

                                width="stretch"

                            )

                        # -------------------------
                        # Excel
                        # -------------------------

                        excel_buffer = io.BytesIO()

                        with pd.ExcelWriter(

                                excel_buffer,

                                engine="openpyxl"

                        ) as writer:

                            df.to_excel(

                                writer,

                                index=False,

                                sheet_name="Results"

                            )

                        excel_buffer.seek(0)

                        with col_excel:

                            st.download_button(

                                label="📊 Download Excel",

                                data=excel_buffer,

                                file_name="query_results.xlsx",

                                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",

                                width="stretch"

                            )


                    else:

                        st.info(
                            "Query executed successfully. No rows returned."
                        )

                else:

                    st.error(result["error"])
                    return

                # =====================================================
                # Explanation
                # =====================================================

                explanation = response.get(
                    "explanation",
                    ""
                )

                if explanation:

                    st.subheader("AI Explanation")

                    st.info(explanation)

                    pdf = PDFExport.create(

                        question,

                        database,

                        response["query"],

                        explanation,

                        row_count,

                        metrics.elapsed()

                    )

                    st.download_button(

                        "📄 Download PDF Report",

                        data=pdf,

                        file_name="AI_SQL_Report.pdf",

                        mime="application/pdf",

                        width="stretch"

                    )

                # =====================================================
                # Execution Metrics
                # =====================================================

                st.divider()

                st.subheader("📊 Execution Metrics")

                c1, c2 = st.columns(2)
                c3, c4 = st.columns(2)

                with c1:

                    st.metric(
                        "Database",
                        database
                    )

                with c2:

                    st.metric(
                        "Rows Returned",
                        row_count
                    )

                with c3:

                    st.metric(
                        "Execution Time",
                        f"{metrics.elapsed()} sec"
                    )

                with c4:

                    st.metric(
                        "Provider",
                        f"{provider}\n{model}"
                    )

            except Exception as e:

                st.error(str(e))

