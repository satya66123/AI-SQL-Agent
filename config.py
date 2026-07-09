"""
config.py
----------
Centralized configuration for AI SQL Agent.
Loads environment variables and exposes application settings.
"""

import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()


class Config:
    """Application Configuration"""

    # ==============================
    # App
    # ==============================
    APP_NAME = "AI SQL Agent"
    VERSION = "1.0.0"

    DEBUG = os.getenv("DEBUG", "False").lower() == "true"

    # ==============================
    # AI Provider
    # ==============================
    DEFAULT_PROVIDER = os.getenv("DEFAULT_PROVIDER", "Ollama")
    DEFAULT_MODEL = os.getenv("DEFAULT_MODEL", "qwen2.5b:1.5")

    # ==============================
    # Ollama
    # ==============================
    OLLAMA_HOST = os.getenv(
        "OLLAMA_HOST",
        "http://localhost:11434"
    )

    # ==============================
    # OpenAI
    # ==============================
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY1", "")

    # ==============================
    # Anthropic
    # ==============================
    ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")

    # ==============================
    # MySQL
    # ==============================
    MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
    MYSQL_PORT = int(os.getenv("MYSQL_PORT", 3306))
    MYSQL_USER = os.getenv("MYSQL_USER", "root")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "")
    MYSQL_DATABASE = os.getenv("MYSQL_DATABASE", "")

    # ==============================
    # MongoDB
    # ==============================
    MONGO_URI = os.getenv(
        "MONGO_URI",
        "mongodb://localhost:27017/"
    )

    MONGO_DATABASE = os.getenv(
        "MONGO_DATABASE",
        ""
    )

    # ==============================
    # Logging
    # ==============================
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

    # ==============================
    # History
    # ==============================
    MAX_HISTORY = int(os.getenv("MAX_HISTORY", 100))

    # ==============================
    # Timeouts
    # ==============================
    REQUEST_TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", 120))


config = Config()