from langchain_core.messages import (
    HumanMessage,
)

from services.llm_service import (
    llm_service,
)


def validate_retrieval(
    query: str,
    retrieved_context: str,
):

    prompt = f"""
You are a retrieval evaluator.

User Query:
{query}

Retrieved Context:
{retrieved_context}

Determine whether the retrieved
context is relevant enough
to answer the query.

Return ONLY:

RELEVANT
or
NOT_RELEVANT
"""

    response = llm_service.invoke([HumanMessage(content=prompt)])

    return response.content.strip().upper() == "RELEVANT"
