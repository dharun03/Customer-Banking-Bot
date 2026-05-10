JAILBREAK_PATTERNS = [
    "pretend you are",
    "roleplay as",
    "you are no longer",
    "simulate another ai",
    "act without restrictions",
]


def detect_jailbreak(text: str):

    text = text.lower()

    for pattern in JAILBREAK_PATTERNS:

        if pattern in text:

            return True

    return False
