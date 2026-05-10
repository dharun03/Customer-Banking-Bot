import re


def detect_pii(text: str):

    patterns = {
        "card_number": r"\b\d{16}\b",
        "aadhaar": r"\b\d{12}\b",
        "cvv": r"\bcvv\s*[:\\-]?\s*\d{3}\b",
        "pan": r"\b[A-Z]{5}[0-9]{4}[A-Z]{1}\b",
    }

    detected = []

    for pii_type, pattern in patterns.items():

        if re.search(pattern, text, re.IGNORECASE):

            detected.append(pii_type)

    return detected
