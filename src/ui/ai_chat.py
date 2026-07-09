import streamlit as st
import pandas as pd

from src.agents.orchestrator import AgentOrchestrator


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

    question = st.text_area(
        "Enter your question",
        placeholder="Example: Show employees earning more than 70000",
        height=120
    )

    if st.button(
        "🚀 Ask AI",
        use_container_width=True
    ):

        if not question.strip():

            st.warning("Please enter a question.")

            st.stop()

        with st.spinner("Generating SQL and executing query..."):

            try:

                orchestrator = AgentOrchestrator()

                response = orchestrator.process(question)

                # -------------------------
                # Generated SQL
                # -------------------------

                st.subheader("Generated SQL")

                st.code(
                    response["query"],
                    language="sql"
                )

                # -------------------------
                # Query Result
                # -------------------------

                result = response["result"]

                if result["success"]:

                    rows = result.get("rows", [])

                    if rows:

                        df = pd.DataFrame(rows)

                        st.subheader("Query Results")

                        st.dataframe(
                            df,
                            use_container_width=True
                        )

                        st.success(
                            f"{len(df)} row(s) returned."
                        )

                    else:

                        st.info("Query executed successfully. No rows returned.")

                else:

                    st.error(result["error"])

                    return

                # -------------------------
                # AI Explanation
                # -------------------------

                explanation = response.get(
                    "explanation",
                    ""
                )

                if explanation:

                    st.subheader("AI Explanation")

                    st.info(explanation)

            except Exception as e:

                st.error(str(e))