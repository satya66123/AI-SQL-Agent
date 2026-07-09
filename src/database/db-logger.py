from src.utils.logger import get_logger

logger = get_logger(
    "DATABASE",
    "database.log"
)

logger.info("Connecting MySQL")

logger.info("Executing SQL")

logger.error("Authentication Failed")