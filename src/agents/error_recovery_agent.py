"""
Error Recovery Agent

Phase 2 Version

Currently acts as a safe pass-through.

In Phase 3 this agent will be upgraded to:

1. Detect SQL syntax errors
2. Ask AI to repair invalid SQL
3. Preserve valid SQL without modifying it
"""


class ErrorRecoveryAgent:

    def __init__(self):
        pass

    # --------------------------------------------------
    # Recover SQL
    # --------------------------------------------------

    def recover(self, sql):

        # Never modify SQL if it is already valid.
        return sql

    # --------------------------------------------------
    # Recover Mongo Query
    # --------------------------------------------------

    def recover_mongo(self, query):

        return query