import re

# PII regex patterns
PII_PATTERNS = {
    "card_number": {
        "pattern": r"\b(?:\d{4}[- ]?){3}\d{4}\b",
        "confidence": 0.98,
    },
    "aadhaar": {
        "pattern": r"\b\d{4}[- ]?\d{4}[- ]?\d{4}\b",
        "confidence": 0.97,
    },
    "pan": {
        "pattern": r"\b[A-Z]{5}[0-9]{4}[A-Z]\b",
        "confidence": 0.99,
    },
    "cvv": {
        "pattern": r"\bcvv\s*[:\-]?\s*\d{3}\b",
        "confidence": 0.95,
    },
    "phone": {
        "pattern": r"\b(?:\+91[- ]?)?[6-9]\d{9}\b",
        "confidence": 0.90,
    },
    "email": {
        "pattern": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",
        "confidence": 0.99,
    },
    "upi_id": {
        "pattern": r"\b[\w.\-_]{2,}@[a-zA-Z]{2,}\b",
        "confidence": 0.88,
    },
    "ifsc": {
        "pattern": r"\b[A-Z]{4}0[A-Z0-9]{6}\b",
        "confidence": 0.94,
    },
    "bank_account": {
        "pattern": r"\b\d{9,18}\b",
        "confidence": 0.70,
    },
}


# Remove spaces and hyphens
def normalize_value(value: str):

    return re.sub(r"[- ]", "", value)


# Basic false positive filtering
def is_valid_match(pii_type: str, value: str):

    normalized = normalize_value(value)

    if pii_type == "aadhaar":

        if normalized.startswith("0000"):
            return False

    if pii_type == "bank_account":

        if len(normalized) < 9:
            return False

    return True


# Detect PII entities
def detect_pii(text: str):

    findings = []

    for pii_type, config in PII_PATTERNS.items():

        pattern = config["pattern"]

        confidence = config["confidence"]

        matches = re.finditer(
            pattern,
            text,
            re.IGNORECASE,
        )

        for match in matches:

            raw_value = match.group()

            normalized = normalize_value(raw_value)

            if not is_valid_match(
                pii_type,
                normalized,
            ):
                continue

            findings.append(
                {
                    "type": pii_type,
                    "value": raw_value,
                    "normalized": normalized,
                    "start": match.start(),
                    "end": match.end(),
                    "confidence": confidence,
                }
            )

    return findings
