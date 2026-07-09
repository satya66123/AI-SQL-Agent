"""
Optimizer Agent

Optimizes AI generated SQL queries before execution.
"""

from src.agents.base_agent import BaseAgent


class OptimizerAgent(BaseAgent):

    def __init__(self):

        super().__init__()

    def optimize(self, sql):

        prompt = f"""
You are an expert MySQL Query Optimizer.

Your task is to optimize the SQL query without changing its result.

Rules:

1. Return ONLY SQL.
2. Do NOT explain anything.
3. Do NOT use Markdown.
4. Do NOT use ```sql.
5. Preserve the same output.
6. Preserve read-only queries.
7. Never generate INSERT, UPDATE, DELETE, DROP, ALTER, CREATE or TRUNCATE.
8. If the query is already optimal, return it unchanged.

SQL Query:

{sql}
"""

        optimized_sql = self.ask_ai(prompt)

        return optimized_sql.strip()

    def process(self, sql):

        return self.optimize(sql)