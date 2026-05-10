import logging
import json

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger("banking_ai")


def log_json(data: dict):

    logger.info(json.dumps(data))
