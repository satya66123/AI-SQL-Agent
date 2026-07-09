from src.agents.optimizer_agent import OptimizerAgent

agent = OptimizerAgent()

sql = """
SELECT *
FROM employees
WHERE salary > 70000;
"""

optimized = agent.optimize(sql)

print("Original SQL")
print(sql)

print()

print("Optimized SQL")
print(optimized)