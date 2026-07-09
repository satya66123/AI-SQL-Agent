"""
MongoDB Query Validator

Responsible for:

1. Cleaning AI output
2. Removing markdown
3. Blocking dangerous MongoDB operations
4. Allowing only read-only queries
"""

import re


class MongoValidator:

    ALLOWED_OPERATIONS = [
        ".find(",
        ".find_one(",
        ".aggregate(",
        ".count_documents(",
        ".estimated_document_count(",
        ".distinct("
    ]

    BLOCKED_OPERATIONS = [
        ".drop(",
        ".delete_one(",
        ".delete_many(",
        ".remove(",
        ".update_one(",
        ".update_many(",
        ".replace_one(",
        ".insert_one(",
        ".insert_many(",
        ".bulk_write(",
        ".create_collection(",
        ".rename(",
    ]

    @staticmethod
    def clean(query: str):

        if query is None:
            return ""

        query = query.replace("```javascript", "")
        query = query.replace("```js", "")
        query = query.replace("```json", "")
        query = query.replace("```", "")

        return query.strip()

    @staticmethod
    def validate(query: str):

        query = MongoValidator.clean(query)

        lower = query.lower()

        # Block dangerous operations
        for operation in MongoValidator.BLOCKED_OPERATIONS:

            if operation in lower:

                return {
                    "success": False,
                    "message": f"Blocked MongoDB operation: {operation}"
                }

        # Allow only safe operations
        for operation in MongoValidator.ALLOWED_OPERATIONS:

            if operation in lower:

                return {
                    "success": True,
                    "query": query
                }

        return {
            "success": False,
            "message": "Only read-only MongoDB queries are allowed."
        }