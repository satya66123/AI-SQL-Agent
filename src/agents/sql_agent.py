from src.agents.base_agent import BaseAgent

from src.database.schema_service import SchemaService
from src.prompts.prompt_builder import PromptBuilder
from src.validators.sql_validator import SQLValidator


class SQLAgent(BaseAgent):

    def __init__(self):

        super().__init__()

        self.schema = SchemaService()

    # ----------------------------------------------------
    # Generate SQL
    # ----------------------------------------------------

    def generate_sql(self, question):

        # Read complete database schema
        schema = self.schema.build_complete_schema()

        # Build AI prompt
        prompt = PromptBuilder.build_sql_prompt(

            schema=schema,

            question=question

        )

        # Generate SQL
        sql = self.ask_ai(prompt)

        print("=" * 80)
        print("GENERATED SQL")
        print(sql)
        print("=" * 80)

        # Validate SQL
        validation = SQLValidator.validate(sql)

        if validation["success"]:

            return validation["sql"]

        raise Exception(validation["message"])

    # ----------------------------------------------------

    def process(self, question):

        return self.generate_sql(question)