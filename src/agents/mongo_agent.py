from src.agents.base_agent import BaseAgent

from src.prompts.prompt_builder import PromptBuilder
from src.database.schema_service import SchemaService

from src.validators.mongo_validator import MongoValidator


class MongoAgent(BaseAgent):

    def __init__(self):

        super().__init__()

        self.schema = SchemaService()

    # ----------------------------------------------------

    def build_schema(self):

        schema_text = ""

        collections = self.schema.get_collections()

        for collection in collections:

            schema_text += f"\nCollection : {collection}\n"

            sample = self.schema.sample_document(collection)

            if sample:

                for key, value in sample.items():

                    schema_text += f"{key} : {type(value).__name__}\n"

        return schema_text

    # ----------------------------------------------------

    def generate_query(self, question):

        schema = self.build_schema()

        prompt = PromptBuilder.build_mongo_prompt(

            schema=schema,

            question=question

        )

        mongo_query = self.ask_ai(prompt)

        print("=" * 80)
        print("RAW MONGO QUERY")
        print(mongo_query)
        print("=" * 80)

        result = MongoValidator.validate(mongo_query)

        if result["success"]:

            return result["query"]

        raise Exception(result["message"])

    # ----------------------------------------------------

    def process(self, question):

        return self.generate_query(question)