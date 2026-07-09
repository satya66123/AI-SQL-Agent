from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

from config import config
from src.utils.logger import get_logger


logger = get_logger(
    "MYSQL",
    "database.log"
)


class MySQLManager:

    def __init__(self):

        self.engine = None

    def connect(self):

        try:

            url = (
                f"mysql+pymysql://"
                f"{config.MYSQL_USER}:"
                f"{config.MYSQL_PASSWORD}@"
                f"{config.MYSQL_HOST}:"
                f"{config.MYSQL_PORT}/"
                f"{config.MYSQL_DATABASE}"
            )

            self.engine = create_engine(url)

            connection = self.engine.connect()

            connection.close()

            logger.info("MySQL Connected")

            return True

        except SQLAlchemyError as e:

            logger.error(e)

            return False