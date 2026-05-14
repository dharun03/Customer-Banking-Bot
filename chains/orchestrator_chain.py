from langchain_core.messages import (
    HumanMessage,
    SystemMessage,
)

from services.llm_service import llm_service

from prompts.agent_prompt import AGENT_SYSTEM_PROMPT

from chains.tool_calling_chain import run_tool_calling_chain

from chains.tool_executor import execute_tools

from memory.hybrid_memory import HybridMemoryManager

from rag.retriever.retrieval_pipeline import (
    run_rag_pipeline,
)

from document_upload.hybrid_retriever import (
    retrieve_document_context,
)

from guardrails.pii_masker import mask_pii

from chains.intent_router_chain import (
    run_intent_chain,
)

from chains.guardrail_chain import (
    run_guardrail_chain,
)


def run_orchestrator(
    query: str,
    session_id: str,
):

    # Mask incoming query
    safe_query = mask_pii(query)

    # Run guardrails
    guardrail_result = run_guardrail_chain(safe_query)

    # Block unsafe queries
    if guardrail_result.status.lower() == "blocked":

        return f"""
Request blocked by security guardrails.

Reason:
{guardrail_result.reason}
"""

    # Run intent routing
    intent_result = run_intent_chain(safe_query)

    # Initialize memory manager
    memory_manager = HybridMemoryManager(session_id)

    # Load memory messages
    memory_messages = memory_manager.get_context_messages()

    # Run FAQ RAG retrieval
    rag_result = run_rag_pipeline(safe_query)

    # Run document retrieval
    document_context = retrieve_document_context(
        query=safe_query,
        session_id=session_id,
    )

    # Store document messages
    document_messages = []

    if document_context:

        document_messages.append(SystemMessage(content=f"""
Document Context:

{document_context}
"""))

    # Store FAQ messages
    rag_messages = []

    if rag_result:

        rag_messages.append(SystemMessage(content=f"""
FAQ Context:

{rag_result['context']}
"""))

    # Add intent routing metadata
    routing_message = SystemMessage(content=f"""
Intent Classification:

Intent: {intent_result.intent}

Sentiment: {intent_result.sentiment}

Confidence: {intent_result.confidence}

Escalation Required:
{intent_result.escalation_required}
""")

    # Run tool calling layer
    initial_response = run_tool_calling_chain(
        safe_query,
        memory_messages,
    )

    # Execute tools
    tool_messages = execute_tools(initial_response)

    # Build final orchestration prompt
    final_messages = [
        SystemMessage(content=AGENT_SYSTEM_PROMPT),
        routing_message,
        *document_messages,
        *rag_messages,
        *memory_messages,
        HumanMessage(content=safe_query),
        initial_response,
        *tool_messages,
    ]

    # Generate final response
    final_response = llm_service.invoke(final_messages)

    # Mask outgoing response
    safe_content = mask_pii(final_response.content)

    # Save conversation memory
    memory_manager.save_context(
        safe_query,
        safe_content,
    )

    return safe_content
