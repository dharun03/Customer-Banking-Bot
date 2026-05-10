import pytest
import requests
import uuid
import json
import time

BASE_URL = "http://localhost:8000/chat"

# Single session to validate long-term conversational memory
SESSION_ID = str(uuid.uuid4())


TEST_CASES = [
    # 1
    "Hi, my name is Rahul Sharma and I have been a customer for 12 years.",
    # 2
    "I noticed an unauthorized transaction of ₹18,500 on my debit card yesterday.",
    # 3
    "Please block my debit card immediately and raise a complaint ticket for this fraud transaction.",
    # 4
    "What is the complaint ticket number for the fraud issue I just reported?",
    # 5
    "I’m really frustrated because this is the second time this has happened to me.",
    # 6
    "Can you also check my last 5 account transactions?",
    # 7
    "I want to apply for a home loan of ₹45 lakhs for 20 years at 8.5% interest. Calculate the EMI.",
    # 8
    "What would be the total interest payable for that loan?",
    # 9
    "Convert 2500 USD to INR using the latest exchange rate.",
    # 10
    "How long does it usually take to resolve fraud-related complaints?",
    # 11
    "I still have not received any update regarding my complaint.",
    # 12
    "Escalate this issue to a senior manager because I’m extremely unhappy with the service.",
    # 13
    "Can you summarize all the issues I have reported so far in this conversation?",
    # 14
    "My registered mobile number also needs to be updated because I lost access to the old number.",
    # 15
    "What documents are required for updating the mobile number linked to my bank account?",
    # 16
    "I also want to know why a maintenance charge was debited from my savings account last month.",
    # 17
    "Please create another complaint ticket for the unnecessary maintenance charge deduction.",
    # 18
    "What are all the active complaint tickets currently open for my account?",
    # 19
    "Do you remember my name and how long I said I’ve been banking with you?",
    # 20
    "Give me a final summary of this entire conversation including complaints, escalation status, EMI calculation, and currency conversion.",
]


@pytest.mark.parametrize(
    "query",
    TEST_CASES,
)
def test_banking_assistant_memory_and_tools(query):

    print("\n" + "=" * 100)

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

    # Optional validation hooks for specific scenarios

    # EMI calculator validation
    if "EMI" in query or "loan" in query:
        assert "emi" in data["answer"].lower() or "monthly" in data["answer"].lower()

    # Currency exchange validation
    if "USD to INR" in query:
        assert "inr" in data["answer"].lower() or "exchange" in data["answer"].lower()

    # Complaint / ticket validation
    if "complaint" in query.lower() or "ticket" in query.lower():
        assert (
            "ticket" in data["answer"].lower() or "complaint" in data["answer"].lower()
        )

    # Memory retention validation
    if "remember my name" in query.lower():
        assert "rahul" in data["answer"].lower()
        assert "12 years" in data["answer"].lower()

    print("\nTEST PASSED")

    print("=" * 100)
