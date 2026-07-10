from src.agents.base_agent import BaseAgent

from src.database.schema_service import SchemaService

from src.prompts.mongo_repair_prompt import MONGO_REPAIR_PROMPT


class MongoRepairAgent(BaseAgent):

    def __init__(self):

        super().__init__()

        self.schema = SchemaService()

    # --------------------------------------------

    def repair(

        self,

        query,

        error

    ):

        schema = self.schema.build_complete_schema()

        prompt = MONGO_REPAIR_PROMPT.format(

            schema=schema,

            query=query,

            error=error

        )

        repaired_query = self.ask_ai(prompt)

        return repaired_query

    # --------------------------------------------

    def process(self, question):

        pass