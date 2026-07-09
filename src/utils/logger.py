"""
Professional Logger
Used across the entire application.
"""

import logging
import os


LOG_FOLDER = "logs"

os.makedirs(LOG_FOLDER, exist_ok=True)


def get_logger(name: str,
               log_file: str = "app.log",
               level=logging.INFO):
    """
    Create and return a logger instance.

    Parameters
    ----------
    name : str
        Logger name

    log_file : str
        Log file name

    level : int
        Logging level
    """

    logger = logging.getLogger(name)

    logger.setLevel(level)

    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    file_handler = logging.FileHandler(
        os.path.join(LOG_FOLDER, log_file),
        encoding="utf-8"
    )

    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()

    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger