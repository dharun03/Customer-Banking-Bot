from guardrails.input_sanitizer import sanitize_input

from guardrails.pii_detector import detect_pii

from guardrails.injection_detector import detect_injection

from guardrails.jailbreak_detector import detect_jailbreak

from guardrails.pii_masker import mask_pii


def validate_query(query: str):

    sanitized_query = sanitize_input(query)

    pii_found = detect_pii(sanitized_query)

    masked_query = mask_pii(sanitized_query)

    if detect_injection(masked_query):

        return {
            "allowed": False,
            "reason": "Prompt injection detected",
        }

    if detect_jailbreak(masked_query):

        return {
            "allowed": False,
            "reason": "Jailbreak attempt detected",
        }

    return {
        "allowed": True,
        "query": masked_query,
        "pii_detected": pii_found,
    }
