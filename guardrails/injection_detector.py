INJECTION_PATTERNS = [
    "ignore previous instructions",
    "reveal system prompt",
    "bypass security",
    "act as admin",
    "developer mode",
    "system prompt",
    "ignore all rules",
]


def detect_injection(text: str):

    text = text.lower()

    for pattern in INJECTION_PATTERNS:

        if pattern in text:

            return True

    return False
