"""
Mongo Query Parser

Supports official MongoDB shell syntax.

Examples

db.employees.find({ salary: { $gt: 70000 } })

db.employees.find({
    department: "IT"
})

db.orders.aggregate([
    {
        $match: {
            status: "Delivered"
        }
    }
])
"""

import ast
import re


class MongoParser:

    # -----------------------------------------------------

    @staticmethod
    def _convert_to_python(text):

        # Quote field names
        text = re.sub(
            r'([{,]\s*)([A-Za-z_][A-Za-z0-9_]*)\s*:',
            r'\1"\2":',
            text
        )

        # Quote Mongo operators
        text = re.sub(
            r'(\$[A-Za-z_][A-Za-z0-9_]*)\s*:',
            r'"\1":',
            text
        )

        # true / false / null
        text = re.sub(r'\btrue\b', "True", text)
        text = re.sub(r'\bfalse\b', "False", text)
        text = re.sub(r'\bnull\b', "None", text)

        return text

    # -----------------------------------------------------

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

    # -----------------------------------------------------

    @staticmethod
    def parse_find(query):

        match = re.search(

            r"find\s*\((.*)\)",

            query,

            re.DOTALL

        )

        if not match:

            raise ValueError("Invalid find() query")

        text = match.group(1).strip()

        if text == "":

            text = "{}"

        text = MongoParser._convert_to_python(text)

        return {

            "operation": "find",

            "query": ast.literal_eval(text)

        }

    # -----------------------------------------------------

    @staticmethod
    def parse_find_one(query):

        match = re.search(

            r"find_one\s*\((.*)\)",

            query,

            re.DOTALL

        )

        if not match:

            raise ValueError("Invalid find_one() query")

        text = match.group(1).strip()

        if text == "":

            text = "{}"

        text = MongoParser._convert_to_python(text)

        return {

            "operation": "find_one",

            "query": ast.literal_eval(text)

        }

    # -----------------------------------------------------

    @staticmethod
    def parse_aggregate(query):

        match = re.search(

            r"aggregate\s*\((.*)\)",

            query,

            re.DOTALL

        )

        if not match:

            raise ValueError("Invalid aggregate() query")

        text = match.group(1).strip()

        text = MongoParser._convert_to_python(text)

        return {

            "operation": "aggregate",

            "pipeline": ast.literal_eval(text)

        }