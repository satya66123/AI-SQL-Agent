from src.agents.sql_agent import SQLAgent


agent = SQLAgent()

sql = agent.generate_sql(

    "Show all employees"

)

print(sql)