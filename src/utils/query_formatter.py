"""
Query Formatter

Formats SQL and MongoDB queries for display.
"""

import sqlparse
import json


class QueryFormatter:

    @staticmethod
    def format_sql(sql: str):

        try:

            return sqlparse.format(

                sql,

                reindent=True,

                keyword_case="upper",

                identifier_case=None,

                strip_comments=True

            )

        except Exception:

            return sql

    # --------------------------------------------------

    @staticmethod
    def format_mongo(query: str):

        return query