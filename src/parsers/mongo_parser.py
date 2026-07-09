"""
Mongo Query Parser

Converts AI generated MongoDB query strings into
Python objects that can be executed.

Current Support

✔ find({})
✔ find({"field":"value"})
✔ find({"salary":{"$gt":70000}})
✔ find_one({})
✔ aggregate([...])

Future

✔ sort()
✔ limit()
✔ skip()
"""

import ast
import re


class MongoParser:

    @staticmethod
    def parse(query):

        query = query.strip()

        if ".find(" in query:

            return MongoParser.parse_find(query)

        elif ".find_one(" in query:

            return MongoParser.parse_find_one(query)

        elif ".aggregate(" in query:

            return MongoParser.parse_aggregate(query)

        raise ValueError("Unsupported Mongo Query")

    # ------------------------------------------------

    @staticmethod
    def parse_find(query):

        match = re.search(r"find\s*\((.*)\)", query, re.DOTALL)

        if not match:

            raise ValueError("Invalid find() query")

        text = match.group(1).strip()

        if text == "":

            text = "{}"

        return {

            "operation": "find",

            "query": ast.literal_eval(text)

        }

    # ------------------------------------------------

    @staticmethod
    def parse_find_one(query):

        match = re.search(r"find_one\s*\((.*)\)", query, re.DOTALL)

        if not match:

            raise ValueError("Invalid find_one() query")

        text = match.group(1).strip()

        if text == "":

            text = "{}"

        return {

            "operation": "find_one",

            "query": ast.literal_eval(text)

        }

    # ------------------------------------------------

    @staticmethod
    def parse_aggregate(query):

        match = re.search(r"aggregate\s*\((.*)\)", query, re.DOTALL)

        if not match:

            raise ValueError("Invalid aggregate() query")

        text = match.group(1).strip()

        return {

            "operation": "aggregate",

            "pipeline": ast.literal_eval(text)

        }