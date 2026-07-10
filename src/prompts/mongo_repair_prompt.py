MONGO_REPAIR_PROMPT = """
You are an expert MongoDB engineer.

The following MongoDB query failed.

Rules:

1. Fix ONLY the MongoDB query.
2. Do NOT change the user's intent.
3. Use ONLY the provided collections and fields.
4. Return ONLY executable MongoDB query.
5. Never explain anything.
6. Never use markdown.

Schema

{schema}

Failed Query

{query}

Database Error

{error}

Return ONLY corrected MongoDB query.
"""