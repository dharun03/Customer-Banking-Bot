import logging
import json
from guardrails.pii_masker import mask_pii

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger("banking_ai")


def sanitize_log_data(data: dict):

    sanitized = {}

    for key, value in data.items():

        if isinstance(value, str):

            sanitized[key] = mask_pii(value)

        else:

            sanitized[key] = value

    return sanitized


def log_json(data: dict):

    safe_data = sanitize_log_data(data)

    logger.info(json.dumps(safe_data))
