"""
Prompt Builder
Builds prompts for different AI tasks.
"""

from src.prompts.sql_prompt import SYSTEM_SQL_PROMPT
from src.prompts.mongo_prompt import SYSTEM_MONGO_PROMPT


class PromptBuilder:

    @staticmethod
    def build_sql_prompt(schema: str, question: str) -> str:
        """
        Build SQL generation prompt.
        """

        return f"""
{SYSTEM_SQL_PROMPT}

==============================
DATABASE SCHEMA
==============================

{schema}

==============================
USER QUESTION
==============================

{question}

==============================
OUTPUT
==============================

Generate ONLY executable MySQL SQL.
Do not include explanations.
Do not use markdown.
Do not use ```sql.
Return only SQL.
""".strip()

    @staticmethod
    def build_mongo_prompt(schema: str, question: str) -> str:
        """
        Build MongoDB generation prompt.
        """

        return f"""
{SYSTEM_MONGO_PROMPT}

==============================
DATABASE SCHEMA
==============================

{schema}

==============================
USER QUESTION
==============================

{question}

==============================
OUTPUT
==============================

Generate ONLY executable MongoDB query.
Do not include explanations.
Do not use markdown.
Return only the MongoDB query.
""".strip()