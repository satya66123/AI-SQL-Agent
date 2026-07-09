import streamlit as st


def show_home():

    st.title("🤖 AI SQL Agent")

    st.markdown("---")

    st.subheader("Welcome")

    st.write(
        """
        AI SQL Agent is an intelligent database assistant.

        Features

        • Natural Language to SQL

        • Natural Language to MongoDB

        • Query Optimization

        • SQL Explanation

        • Analytics

        • Charts

        • Reports

        • Multi AI Providers
        """
    )