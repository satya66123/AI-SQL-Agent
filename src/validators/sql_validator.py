import re


class SQLValidator:

    ALLOWED_COMMANDS = [

        "SELECT",

        "SHOW",

        "DESCRIBE",

        "DESC",

        "EXPLAIN"

    ]

    BLOCKED_COMMANDS = [

        "DROP",

        "DELETE",

        "UPDATE",

        "INSERT",

        "ALTER",

        "TRUNCATE",

        "CREATE",

        "REPLACE",

        "GRANT",

        "REVOKE"

    ]

    @staticmethod
    def clean(sql: str):

        sql = sql.replace("```sql", "")

        sql = sql.replace("```", "")

        sql = sql.strip()

        return sql

    @staticmethod
    def validate(sql: str):

        sql = SQLValidator.clean(sql)

        upper = sql.upper()

        for command in SQLValidator.BLOCKED_COMMANDS:

            if re.search(rf"\b{command}\b", upper):

                return {

                    "success": False,

                    "message": f"{command} statements are blocked."

                }

        allowed = False

        for command in SQLValidator.ALLOWED_COMMANDS:

            if upper.startswith(command):

                allowed = True

                break

        if not allowed:

            return {

                "success": False,

                "message": "Only read-only SQL statements are allowed."

            }

        return {

            "success": True,

            "sql": sql

        }