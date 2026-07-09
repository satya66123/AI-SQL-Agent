from src.database.mysql_service import MySQLService
from src.database.mongodb_service import MongoDBService


class SchemaService:

    def __init__(self):

        self.mysql = MySQLService()

        self.mongo = MongoDBService()

    # =====================================================
    # MYSQL
    # =====================================================

    def get_tables(self):

        result = self.mysql.execute_query("SHOW TABLES")

        if result["success"]:

            key = list(result["rows"][0].keys())[0]

            return [

                row[key]

                for row in result["rows"]

            ]

        return []

    # -----------------------------------------------------

    def get_columns(self, table):

        result = self.mysql.execute_query(

            f"DESCRIBE {table}"

        )

        if result["success"]:

            return result["rows"]

        return []

    # -----------------------------------------------------

    def get_primary_keys(self, table):

        query = f"""
        SHOW KEYS
        FROM {table}
        WHERE Key_name='PRIMARY'
        """

        result = self.mysql.execute_query(query)

        if result["success"]:

            return [

                row["Column_name"]

                for row in result["rows"]

            ]

        return []

    # -----------------------------------------------------

    def get_foreign_keys(self):

        query = """
        SELECT

            TABLE_NAME,

            COLUMN_NAME,

            REFERENCED_TABLE_NAME,

            REFERENCED_COLUMN_NAME

        FROM information_schema.KEY_COLUMN_USAGE

        WHERE

            TABLE_SCHEMA = DATABASE()

        AND

            REFERENCED_TABLE_NAME IS NOT NULL;
        """

        result = self.mysql.execute_query(query)

        if result["success"]:

            return result["rows"]

        return []

    # -----------------------------------------------------

    def build_complete_schema(self):

        schema = ""

        tables = self.get_tables()

        for table in tables:

            schema += "\n"

            schema += "=" * 60

            schema += "\n"

            schema += f"TABLE : {table}\n"

            schema += "=" * 60

            schema += "\n"

            columns = self.get_columns(table)

            primary = self.get_primary_keys(table)

            for column in columns:

                schema += (

                    f"{column['Field']}"

                    f" ({column['Type']})"

                )

                if column["Field"] in primary:

                    schema += " PRIMARY KEY"

                schema += "\n"

        schema += "\n"

        schema += "=" * 60

        schema += "\n"

        schema += "RELATIONSHIPS\n"

        schema += "=" * 60

        schema += "\n"

        relations = self.get_foreign_keys()

        for relation in relations:

            schema += (

                f"{relation['TABLE_NAME']}."

                f"{relation['COLUMN_NAME']}"

                " --> "

                f"{relation['REFERENCED_TABLE_NAME']}."

                f"{relation['REFERENCED_COLUMN_NAME']}\n"

            )

        return schema

    # =====================================================
    # MONGODB
    # =====================================================

    def get_collections(self):

        return self.mongo.list_collections()

    # -----------------------------------------------------

    def sample_document(self, collection):

        return self.mongo.sample_document(collection)