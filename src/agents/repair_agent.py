from src.agents.base_agent import BaseAgent

from src.database.schema_service import SchemaService

from src.prompts.repair_prompt import REPAIR_PROMPT


class RepairAgent(BaseAgent):

    def __init__(self):

        super().__init__()

        self.schema = SchemaService()

    # --------------------------------------------

    def repair(self, sql, error):

        schema = self.schema.build_complete_schema()

        prompt = REPAIR_PROMPT.format(

            schema=schema,

            sql=sql,

            error=error

        )

        repaired_sql = self.ask_ai(prompt)

        return repaired_sql

    # --------------------------------------------

    def process(self, question):

        pass