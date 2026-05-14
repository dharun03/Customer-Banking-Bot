import re

# PII patterns
PII_PATTERNS = {
    "card_number": r"\b(?:\d{4}[- ]?){3}\d{4}\b",
    "aadhaar": r"\b\d{4}[- ]?\d{4}[- ]?\d{4}\b",
    "pan": r"\b[A-Z]{5}[0-9]{4}[A-Z]\b",
    "cvv": r"\bcvv\s*[:\-]?\s*\d{3}\b",
    "phone": r"\b(?:\+91[- ]?)?[6-9]\d{9}\b",
    "email": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",
    "upi_id": r"\b[\w.\-_]{2,}@[a-zA-Z]{2,}\b",
    "ifsc": r"\b[A-Z]{4}0[A-Z0-9]{6}\b",
    "bank_account": r"\b\d{9,18}\b",
}


# Remove spaces and hyphens
def normalize_value(value: str):

    return re.sub(r"[- ]", "", value)


# Mask card numbers
def mask_card(card: str):

    normalized = normalize_value(card)

    return "************" + normalized[-4:]


# Mask Aadhaar
def mask_aadhaar(aadhaar: str):

    normalized = normalize_value(aadhaar)

    return "XXXXXXXX" + normalized[-4:]


# Mask PAN
def mask_pan(pan: str):

    return pan[:3] + "XXXX" + pan[-3:]


# Mask CVV
def mask_cvv(_):

    return "***"


# Mask phone number
def mask_phone(phone: str):

    normalized = normalize_value(phone)

    return "******" + normalized[-4:]


# Mask email
def mask_email(email: str):

    parts = email.split("@")

    username = parts[0]

    domain = parts[1]

    return username[:2] + "***@" + domain


# Mask UPI ID
def mask_upi(upi: str):

    parts = upi.split("@")

    username = parts[0]

    provider = parts[1]

    return username[:2] + "***@" + provider


# Mask IFSC
def mask_ifsc(ifsc: str):

    return ifsc[:4] + "******"


# Mask bank account
def mask_bank_account(account: str):

    normalized = normalize_value(account)

    return "********" + normalized[-4:]


MASKING_FUNCTIONS = {
    "card_number": mask_card,
    "aadhaar": mask_aadhaar,
    "pan": mask_pan,
    "cvv": mask_cvv,
    "phone": mask_phone,
    "email": mask_email,
    "upi_id": mask_upi,
    "ifsc": mask_ifsc,
    "bank_account": mask_bank_account,
}


def mask_pii(text: str):

    masked_text = text

    for pii_type, pattern in PII_PATTERNS.items():

        def replacer(match):

            value = match.group()

            return MASKING_FUNCTIONS[pii_type](value)

        masked_text = re.sub(
            pattern,
            replacer,
            masked_text,
            flags=re.IGNORECASE,
        )

    return masked_text
