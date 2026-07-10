from src.agents.sql_agent import SQLAgent
from src.agents.mongo_agent import MongoAgent
from src.agents.optimizer_agent import OptimizerAgent
from src.agents.explanation_agent import ExplanationAgent
from src.agents.error_recovery_agent import ErrorRecoveryAgent
from src.agents.repair_agent import RepairAgent

from src.database.query_service import QueryService

from src.validators.sql_validator import SQLValidator
from src.validators.mongo_validator import MongoValidator

from src.parsers.mongo_parser import MongoParser


class AgentOrchestrator:

    def __init__(self):

        self.sql_agent = SQLAgent()

        self.mongo_agent = MongoAgent()

        self.optimizer = OptimizerAgent()

        self.recovery = ErrorRecoveryAgent()

        self.query_service = QueryService()

        self.explainer = ExplanationAgent()

        self.repair_agent = RepairAgent()


    # =====================================================
    # DEFAULT PROCESS
    # =====================================================

    def process(self, question):

        # Default to MySQL for now.
        # Later we'll automatically route based on the selected database.

        return self.process_sql(question)



    # =====================================================
    # MYSQL
    # =====================================================



    def process_sql(self, question):

            try:

                # Step 1 - Generate SQL
                sql = self.sql_agent.generate_sql(question)

                print("=" * 80)
                print("RAW SQL")
                print(sql)

                # Step 2 - Optimize
                optimized = self.optimizer.optimize(sql)

                print("=" * 80)
                print("OPTIMIZED SQL")
                print(optimized)

                # Step 3 - Validate
                validation = SQLValidator.validate(optimized)

                print("=" * 80)
                print("VALIDATED SQL")
                print(validation)

                if not validation["success"]:
                    return {

                        "success": False,

                        "error": validation["message"]

                    }

                validated_sql = validation["sql"]

                # Step 4 - Recovery
                #recovered_sql = self.recovery.recover(validated_sql)
                recovered_sql = validated_sql

                print("=" * 80)
                print("RECOVERED SQL")
                print(recovered_sql)

                # Step 5 - Execute
                # Step 5 - Execute
                repairable_errors = [

                    "unknown column",

                    "unknown table",

                    "doesn't exist",

                    "syntax",

                    "column",

                    "table"

                ]
                result = self.query_service.execute_sql(recovered_sql)

                # --------------------------------------
                # AI SQL Repair
                # --------------------------------------

                if not result["success"]:

                    error = result["error"].lower()

                    if any(

                            item in error

                            for item in repairable_errors

                    ):

                        repaired_sql = self.repair_agent.repair(

                            recovered_sql,

                            result["error"]

                        )

                        print("=" * 80)
                        print("REPAIRED SQL")
                        print(repaired_sql)
                        print("=" * 80)

                        repaired = SQLValidator.validate(

                            repaired_sql

                        )

                        if repaired["success"]:
                            recovered_sql = repaired["sql"]

                            result = self.query_service.execute_sql(

                                recovered_sql

                            )

                # Step 6 - Explain
                explanation = ""

                if result["success"]:
                    explanation = self.explainer.explain(

                        question,

                        recovered_sql,

                        len(result.get("rows", []))

                    )

                return {

                    "success": result["success"],

                    "database": "MySQL",

                    "question": question,

                    "query": recovered_sql,

                    "result": result,

                    "explanation": explanation

                }

            except Exception as e:

                return {

                    "success": False,

                    "error": str(e)

                }

    # =====================================================
    # MONGODB
    # =====================================================

    def process_mongo(
        self,
        question,
        collection
    ):

        try:

            mongo_query = self.mongo_agent.process(
                question,
                collection
            )

            validation = MongoValidator.validate(
                mongo_query
            )

            if not validation["success"]:

                return {

                    "success": False,

                    "error": validation["message"]

                }

            mongo_query = validation["query"]

            parsed = MongoParser.parse(
                mongo_query
            )

            operation = parsed["operation"]

            if operation == "find":

                result = self.query_service.execute_mongo(

                    collection,

                    parsed["query"]

                )

            elif operation == "find_one":

                result = self.query_service.execute_mongo_find_one(

                    collection,

                    parsed["query"]

                )

            elif operation == "aggregate":

                result = self.query_service.execute_mongo_aggregate(

                    collection,

                    parsed["pipeline"]

                )

            else:

                return {

                    "success": False,

                    "error": "Unsupported MongoDB operation."

                }

            explanation = ""

            if result["success"]:

                if "rows" in result:

                    row_count = len(result["rows"])

                elif "row" in result:

                    row_count = 1 if result["row"] else 0

                else:

                    row_count = 0

                explanation = self.explainer.explain(

                    question,

                    mongo_query,

                    row_count

                )

            return {

                "success": result["success"],

                "database": "MongoDB",

                "question": question,

                "query": mongo_query,

                "result": result,

                "explanation": explanation

            }

        except Exception as e:

            return {

                "success": False,

                "error": str(e)

            }