from pymongo import MongoClient

from config import config
from src.utils.logger import get_logger


logger = get_logger(
    "MONGODB",
    "database.log"
)


class MongoDBManager:

    def __init__(self):

        self.client = None

    def connect(self):

        try:

            self.client = MongoClient(
                config.MONGO_URI
            )

            self.client.server_info()

            logger.info("MongoDB Connected")

            return True

        except Exception as e:

            logger.error(e)

            return False