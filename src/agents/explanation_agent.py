from src.ai.factory import ProviderFactory


class ExplanationAgent:

    def __init__(self):

        self.provider = ProviderFactory.get_provider()

    def explain(self, question, sql, rows):

        prompt = f"""
You are an AI database assistant.

User Question:
{question}

Generated SQL:
{sql}

Rows Returned:
{rows}

Explain in simple English:

1. What the SQL does.
2. Why this SQL was generated.
3. What the returned result means.

Keep the explanation under 100 words.
"""

        return self.provider.generate(prompt)