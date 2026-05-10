from guardrails.input_sanitizer import sanitize_input

from guardrails.pii_detector import detect_pii

from guardrails.injection_detector import detect_injection

from guardrails.jailbreak_detector import detect_jailbreak


def validate_query(query: str):

    sanitized_query = sanitize_input(query)

    pii_found = detect_pii(sanitized_query)

    if pii_found:

        return {"allowed": False, "reason": f"PII detected: {pii_found}"}

    if detect_injection(sanitized_query):

        return {"allowed": False, "reason": "Prompt injection detected"}

    if detect_jailbreak(sanitized_query):

        return {"allowed": False, "reason": "Jailbreak attempt detected"}

    return {"allowed": True, "query": sanitized_query}
