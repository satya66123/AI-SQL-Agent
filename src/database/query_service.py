from src.database.mysql_service import MySQLService
from src.database.mongodb_service import MongoDBService


class QueryService:

    def __init__(self):

        self.mysql = MySQLService()

        self.mongo = MongoDBService()

    # =====================================================
    # MYSQL
    # =====================================================

    def execute_sql(self, query):
        print("=" * 80)
        print("SQL SENT TO MYSQL")
        print(query)
        print("=" * 80)

        return self.mysql.execute_query(query)
    # =====================================================
    # MONGODB
    # =====================================================

    def execute_mongo(self, collection, query):

        return self.mongo.execute_find(
            collection,
            query
        )

    def execute_mongo_find_one(self, collection, query):

        return self.mongo.execute_find_one(
            collection,
            query
        )

    def execute_mongo_aggregate(self, collection, pipeline):

        return self.mongo.execute_aggregate(
            collection,
            pipeline
        )

    def count_documents(self, collection, query=None):

        return self.mongo.count_documents(
            collection,
            query
        )

    def distinct(self, collection, field):

        return self.mongo.distinct(
            collection,
            field
        )

    # =====================================================
    # SCHEMA
    # =====================================================

    def get_collections(self):

        return self.mongo.list_collections()

    def sample_document(self, collection):

        return self.mongo.sample_document(
            collection
        )