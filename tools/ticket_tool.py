from langchain_core.tools import tool

import uuid
import json
from datetime import datetime


@tool
def ticket_creation_tool(
    customer_query: str,
    priority: str,
    sentiment: str,
    escalation_required: bool,
):
    """
    Create and store complaint tickets.
    """

    ticket = {
        "ticket_id": f"TICKET-{uuid.uuid4().hex[:8].upper()}",
        "timestamp": datetime.utcnow().isoformat(),
        "customer_query": customer_query,
        "priority": priority,
        "sentiment": sentiment,
        "escalation_required": escalation_required,
        "status": "OPEN",
    }

    try:

        with open("data/tickets.json", "r") as file:
            tickets = json.load(file)

    except:
        tickets = []

    tickets.append(ticket)

    with open("data/tickets.json", "w") as file:
        json.dump(tickets, file, indent=2)

    return ticket
