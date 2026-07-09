from src.database.mysql_manager import MySQLManager
from src.database.mongodb_manager import MongoDBManager


class ConnectionManager:

    def __init__(self):

        self.mysql = MySQLManager()

        self.mongo = MongoDBManager()

    def connect(self, database):

        if database == "MySQL":

            return self.mysql.connect()

        elif database == "MongoDB":

            return self.mongo.connect()

        return False