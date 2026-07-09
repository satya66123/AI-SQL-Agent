from src.utils.logger import get_logger

logger = get_logger(
    "AI",
    "ai.log"
)

logger.info("OpenAI Provider Loaded")

logger.info("Ollama Connected")

logger.error("Model Not Found")