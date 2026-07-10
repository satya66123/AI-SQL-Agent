import streamlit as st
import pandas as pd


class ChartGenerator:

    @staticmethod
    def show(df: pd.DataFrame):

        if df.empty:
            return

        st.divider()

        st.subheader("📊 Data Visualization")

        # ----------------------------------------
        # Numeric columns
        # ----------------------------------------

        numeric_columns = list(
            df.select_dtypes(include=["number"]).columns
        )

        if not numeric_columns:

            st.info("No numeric columns available for charts.")

            return

        # ----------------------------------------
        # Candidate X columns
        # ----------------------------------------

        candidate_columns = []

        for col in df.columns:

            lower = col.lower()

            # Skip ID columns
            if "id" in lower:
                continue

            candidate_columns.append(col)

        # If every column is an ID, use first column
        if not candidate_columns:

            candidate_columns = list(df.columns)

        # ----------------------------------------
        # Default X column
        # ----------------------------------------

        default_x = candidate_columns[0]

        # ----------------------------------------
        # Default Y column
        # Prefer salary, amount, price, total...
        # ----------------------------------------

        priority = [
            "salary",
            "amount",
            "price",
            "total",
            "count",
            "quantity"
        ]

        default_y = numeric_columns[0]

        for p in priority:

            for col in numeric_columns:

                if p in col.lower():

                    default_y = col

                    break

        # ----------------------------------------
        # User selection
        # ----------------------------------------

        x_column = st.selectbox(

            "X-Axis",

            candidate_columns,

            index=0,

            key="chart_x"

        )

        y_column = st.selectbox(

            "Y-Axis",

            numeric_columns,

            index=numeric_columns.index(default_y),

            key="chart_y"

        )

        chart = st.selectbox(

            "Chart Type",

            [

                "Bar Chart",

                "Line Chart",

                "Area Chart"

            ],

            key="chart_type"

        )

        chart_df = df.set_index(x_column)

        # ----------------------------------------
        # Draw Chart
        # ----------------------------------------

        if chart == "Bar Chart":

            st.bar_chart(
                chart_df[y_column],
                width="stretch"
            )

        elif chart == "Line Chart":

            st.line_chart(
                chart_df[y_column],
                width="stretch"
            )

        else:

            st.area_chart(
                chart_df[y_column],
                width="stretch"
            )