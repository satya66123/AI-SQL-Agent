from pymongo import MongoClient
from pymongo.errors import PyMongoError

from config import config
from src.utils.logger import get_logger

logger = get_logger(
    "MONGODB",
    "database.log"
)


class MongoDBService:

    def __init__(self):

        self.client = MongoClient(config.MONGO_URI)

        self.db = self.client[config.MONGO_DATABASE]

    # -------------------------------------------------------
    # Get Database
    # -------------------------------------------------------

    def get_database(self):

        return self.db

    # -------------------------------------------------------
    # List Collections
    # -------------------------------------------------------

    def list_collections(self):

        try:

            collections = self.db.list_collection_names()

            logger.info("Collections Retrieved")

            return collections

        except PyMongoError as e:

            logger.error(e)

            return []

    # -------------------------------------------------------
    # Sample Document
    # -------------------------------------------------------

    def sample_document(self, collection_name):

        try:

            document = self.db[collection_name].find_one()

            if document:

                document["_id"] = str(document["_id"])

            logger.info(f"Sample document from {collection_name}")

            return document

        except Exception as e:

            logger.error(e)

            return None

    # -------------------------------------------------------
    # Find
    # -------------------------------------------------------

    def execute_find(self, collection_name, query):

        try:

            collection = self.db[collection_name]

            result = list(
                collection.find(query)
            )

            for row in result:

                if "_id" in row:

                    row["_id"] = str(row["_id"])

            logger.info("Mongo Find Executed")

            return {

                "success": True,

                "rows": result

            }

        except Exception as e:

            logger.error(e)

            return {

                "success": False,

                "error": str(e)

            }

    # -------------------------------------------------------
    # Find One
    # -------------------------------------------------------

    def execute_find_one(self, collection_name, query):

        try:

            collection = self.db[collection_name]

            result = collection.find_one(query)

            if result:

                result["_id"] = str(result["_id"])

            logger.info("Mongo Find One Executed")

            return {

                "success": True,

                "row": result

            }

        except Exception as e:

            logger.error(e)

            return {

                "success": False,

                "error": str(e)

            }

    # -------------------------------------------------------
    # Aggregate
    # -------------------------------------------------------

    def execute_aggregate(self, collection_name, pipeline):

        try:

            collection = self.db[collection_name]

            result = list(
                collection.aggregate(pipeline)
            )

            for row in result:

                if "_id" in row:

                    row["_id"] = str(row["_id"])

            logger.info("Mongo Aggregate Executed")

            return {

                "success": True,

                "rows": result

            }

        except Exception as e:

            logger.error(e)

            return {

                "success": False,

                "error": str(e)

            }

    # -------------------------------------------------------
    # Count Documents
    # -------------------------------------------------------

    def count_documents(self, collection_name, query=None):

        try:

            if query is None:

                query = {}

            collection = self.db[collection_name]

            count = collection.count_documents(query)

            logger.info("Mongo Count Executed")

            return {

                "success": True,

                "count": count

            }

        except Exception as e:

            logger.error(e)

            return {

                "success": False,

                "error": str(e)

            }

    # -------------------------------------------------------
    # Distinct Values
    # -------------------------------------------------------

    def distinct(self, collection_name, field):

        try:

            collection = self.db[collection_name]

            values = collection.distinct(field)

            logger.info("Mongo Distinct Executed")

            return {

                "success": True,

                "values": values

            }

        except Exception as e:

            logger.error(e)

            return {

                "success": False,

                "error": str(e)

            }