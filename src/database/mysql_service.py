import pymysql

from config import config
from src.utils.logger import get_logger

logger = get_logger("MYSQL", "database.log")


class MySQLService:

    def __init__(self):

        self.connection = None

    def connect(self):

        if self.connection:
            return self.connection

        self.connection = pymysql.connect(
            host=config.MYSQL_HOST,
            port=config.MYSQL_PORT,
            user=config.MYSQL_USER,
            password=config.MYSQL_PASSWORD,
            database=config.MYSQL_DATABASE,
            cursorclass=pymysql.cursors.DictCursor
        )

        logger.info("Connected to MySQL")

        return self.connection

    def execute_query(self, query):

        try:

            conn = self.connect()

            with conn.cursor() as cursor:

                cursor.execute(query)

                rows = cursor.fetchall()

                columns = []

                if cursor.description:

                    columns = [

                        column[0]

                        for column in cursor.description

                    ]

            logger.info(f"Executed SQL : {query}")

            return {

                "success": True,

                "columns": columns,

                "rows": rows

            }

        except Exception as e:

            logger.error(e)

            return {

                "success": False,

                "error": str(e)

            }