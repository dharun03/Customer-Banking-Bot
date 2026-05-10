import pytest

import requests

import uuid

import json

import time

BASE_URL = "http://localhost:8000/chat"

SESSION_ID = str(uuid.uuid4())


TEST_CASES = [
    (
        "Tool Usage",
        "I want to report an unauthorized transaction.",
    ),
    (
        "Tool Usage",
        "What is the status of my complaint #CS-8821?",
    ),
    (
        "Tool Usage",
        "I’m extremely unhappy with your service.",
    ),
    (
        "Tool Usage",
        "How do I block my lost debit card?",
    ),
    (
        "Tool Usage",
        "Transfer me to a manager right now.",
    ),
    (
        "Tool Usage",
        "Why was a maintenance charge debited from my account?",
    ),
    (
        "Tool Usage",
        "Check my last 5 transactions.",
    ),
    (
        "FAQ / Follow-up",
        "I filed a complaint 10 days ago and nobody responded.",
    ),
    (
        "FAQ / Follow-up",
        "Can you waive the late payment fee on my credit card?",
    ),
    (
        "FAQ / Follow-up",
        "I need help updating my registered mobile number.",
    ),
    (
        "FAQ / Follow-up",
        "Your ATM ate my card and didn’t return it.",
    ),
    (
        "FAQ / Follow-up",
        "I want to close my account. What is the process?",
    ),
    (
        "FAQ / Follow-up",
        "Why is my net banking locked?",
    ),
    (
        "FAQ / Follow-up",
        "I received an SMS about a transaction I didn’t make.",
    ),
    (
        "Multi-turn",
        "Escalate this — the branch staff was rude to me.",
    ),
    (
        "Multi-turn",
        "How long does an NEFT refund take?",
    ),
    (
        "Multi-turn",
        "Can I get a duplicate statement for the last 6 months?",
    ),
    (
        "Multi-turn",
        "My cheque was bounced but I have sufficient balance.",
    ),
    (
        "Multi-turn",
        "I’ve been a customer for 15 years and this is unacceptable.",
    ),
    (
        "Multi-turn",
        "Summarize all open complaints for my account.",
    ),
]


@pytest.mark.parametrize(
    "category,query",
    TEST_CASES,
)
def test_banking_assistant(
    category,
    query,
):

    print("\n" + "=" * 100)

    print(f"CATEGORY: {category}")

    print(f"QUERY: {query}")

    payload = {
        "query": query,
        "session_id": SESSION_ID,
    }

    start_time = time.time()

    response = requests.post(
        BASE_URL,
        json=payload,
        timeout=120,
    )

    end_time = time.time()

    latency = round(
        end_time - start_time,
        2,
    )

    print(f"\nSTATUS CODE: {response.status_code}")

    assert response.status_code == 200

    data = response.json()

    print("\nRESPONSE:\n")

    print(
        json.dumps(
            data,
            indent=2,
            ensure_ascii=False,
        )
    )

    print(f"\nLATENCY: {latency} sec")

    required_fields = [
        "intent",
        "sentiment",
        "confidence",
        "escalation_required",
        "answer",
    ]

    for field in required_fields:

        assert field in data

    assert isinstance(
        data["intent"],
        str,
    )

    assert isinstance(
        data["sentiment"],
        str,
    )

    assert isinstance(
        data["confidence"],
        (int, float),
    )

    assert isinstance(
        data["escalation_required"],
        bool,
    )

    assert isinstance(
        data["answer"],
        str,
    )

    assert len(data["answer"]) > 0

    print("\nTEST PASSED")

    print("=" * 100)
