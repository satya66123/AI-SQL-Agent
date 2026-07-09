"""
MongoDB AI Agent

Responsible for:

1. Read MongoDB schema
2. Read conversation history
3. Build prompt
4. Send prompt to selected AI provider
5. Validate generated query
6. Return MongoDB query
"""

from src.agents.base_agent import BaseAgent
from src.agents.memory_agent import MemoryAgent

from src.prompts.prompt_builder import PromptBuilder
from src.database.schema_service import SchemaService

from src.validators.mongo_validator import MongoValidator


class MongoAgent(BaseAgent):

    def __init__(self):

        super().__init__()

        self.schema = SchemaService()

        self.memory = MemoryAgent()

    # ----------------------------------------------------
    # Build MongoDB Schema
    # ----------------------------------------------------

    def build_schema(self):

        schema_text = ""

        collections = self.schema.get_collections()

        for collection in collections:

            schema_text += f"\nCollection : {collection}\n"

            sample = self.schema.sample_document(collection)

            if sample:

                for key, value in sample.items():

                    schema_text += (

                        f"{key} : {type(value).__name__}\n"

                    )

        return schema_text

    # ----------------------------------------------------
    # Generate Mongo Query
    # ----------------------------------------------------

    def generate_query(self, question):

        # Save user question
        self.memory.save_user_message(question)

        # Build schema
        schema = self.build_schema()

        # Add previous conversation
        context_question = self.memory.build_prompt(question)

        # Build final prompt
        prompt = PromptBuilder.build_mongo_prompt(

            schema=schema,

            question=context_question

        )

        # Ask AI
        mongo_query = self.ask_ai(prompt)

        # Save AI response
        self.memory.save_assistant_message(mongo_query)

        # Validate query
        result = MongoValidator.validate(mongo_query)

        if result["success"]:

            return result["query"]

        raise Exception(result["message"])

    # ----------------------------------------------------

    def process(self, question):

        return self.generate_query(question)