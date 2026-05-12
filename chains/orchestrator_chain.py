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


def run_orchestrator(
    query: str,
    session_id: str,
):

    memory_manager = HybridMemoryManager(session_id)

    memory_messages = memory_manager.get_context_messages()

    rag_result = run_rag_pipeline(query)

    document_context = retrieve_document_context(
        query=query,
        session_id=session_id,
    )

    document_messages = []

    if document_context:

        document_messages.append(SystemMessage(content=f"""
    Document Context:

    {document_context}
    """))

    rag_messages = []

    if rag_result:

        rag_messages.append(SystemMessage(content=f"""
    FAQ Context:

    {rag_result['context']}
    """))

    initial_response = run_tool_calling_chain(
        query,
        memory_messages,
    )

    tool_messages = execute_tools(initial_response)

    final_messages = [
        SystemMessage(content=AGENT_SYSTEM_PROMPT),
        *document_messages,
        *rag_messages,
        *memory_messages,
        HumanMessage(content=query),
        initial_response,
        *tool_messages,
    ]

    final_response = llm_service.invoke(final_messages)

    content = final_response.content

    memory_manager.save_context(
        query,
        content,
    )

    return content
