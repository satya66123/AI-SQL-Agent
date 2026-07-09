from src.validators.sql_validator import SQLValidator

queries = [

    "SELECT * FROM employees",

    "DROP TABLE employees",

    "DELETE FROM employees",

    "UPDATE employees SET salary=1000",

    "SHOW TABLES",

    "DESCRIBE employees"

]

for query in queries:

    result = SQLValidator.validate(query)

    print(query)

    print(result)

    print("-" * 50)