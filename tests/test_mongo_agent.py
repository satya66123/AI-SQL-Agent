from src.agents.mongo_agent import MongoAgent

agent = MongoAgent()

query = agent.process(

    "Show all employees"

)

print(query)