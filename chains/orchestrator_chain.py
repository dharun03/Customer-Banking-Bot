from langchain_core.messages import (
    HumanMessage,
    SystemMessage,
)

from services.llm_service import llm

from prompts.agent_prompt import AGENT_SYSTEM_PROMPT

from chains.tool_calling_chain import run_tool_calling_chain

from chains.tool_executor import execute_tools

from memory.hybrid_memory import HybridMemoryManager


def run_orchestrator(
    query: str,
    session_id: str,
):

    memory_manager = HybridMemoryManager(session_id)

    memory_messages = memory_manager.get_context_messages()

    initial_response = run_tool_calling_chain(
        query,
        memory_messages,
    )

    tool_messages = execute_tools(initial_response)

    final_messages = [
        SystemMessage(content=AGENT_SYSTEM_PROMPT),
        *memory_messages,
        HumanMessage(content=query),
        initial_response,
        *tool_messages,
    ]

    final_response = llm.invoke(final_messages)

    content = final_response.content

    memory_manager.save_context(
        query,
        content,
    )

    return content
