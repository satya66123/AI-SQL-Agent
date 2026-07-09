from src.agents.base_agent import BaseAgent
from src.agents.memory_agent import MemoryAgent

from src.database.schema_service import SchemaService

from src.prompts.prompt_builder import PromptBuilder

from src.validators.sql_validator import SQLValidator


class SQLAgent(BaseAgent):

    def __init__(self):

        super().__init__()

        self.schema = SchemaService()

        self.memory = MemoryAgent()

    # ----------------------------------------------------
    # Generate SQL
    # ----------------------------------------------------

    def generate_sql(self, question):

        # Save current user question
        self.memory.save_user_message(question)

        # Build schema
        schema = self.schema.build_complete_schema()

        # Build question with previous context
        context_question = self.memory.build_prompt(question)

        # Build prompt
        prompt = PromptBuilder.build_sql_prompt(

            schema=schema,

            question=context_question

        )

        # Ask AI
        sql = self.ask_ai(prompt)

        print("RAW AI SQL")
        print(sql)

        # Save AI response
        self.memory.save_assistant_message(sql)

        # Validate SQL
        result = SQLValidator.validate(sql)

        if result["success"]:

            return result["sql"]

        raise Exception(result["message"])

    # ----------------------------------------------------
    # Build Database Schema
    # ----------------------------------------------------

    def build_schema(self):

        tables = self.schema.get_tables()

        schema_text = ""

        for table in tables:

            schema_text += f"\nTable : {table}\n"

            columns = self.schema.get_columns(table)

            for column in columns:

                schema_text += (

                    f"{column['Field']} "

                    f"{column['Type']}\n"

                )

        return schema_text

    # ----------------------------------------------------

    def process(self, question):

        return self.generate_sql(question)