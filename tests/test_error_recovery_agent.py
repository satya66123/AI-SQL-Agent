from src.agents.error_recovery_agent import ErrorRecoveryAgent

agent = ErrorRecoveryAgent()

sql = """
SELECT *
FROM employee;
"""

print(agent.recover(sql))