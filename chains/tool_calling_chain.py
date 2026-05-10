from langchain_core.messages import (
    HumanMessage,
    SystemMessage,
)

from services.llm_service import llm_service

from tools.tools_registry import TOOLS

from prompts.agent_prompt import AGENT_SYSTEM_PROMPT


def run_tool_calling_chain(
    query: str,
    memory_messages: list,
):

    messages = [
        SystemMessage(content=AGENT_SYSTEM_PROMPT),
        *memory_messages,
        HumanMessage(content=query),
    ]

    try:

        llm_with_tools = llm_service.primary_llm.bind_tools(TOOLS)

        response = llm_with_tools.invoke(messages)

        return response

    except Exception as openai_error:

        print(f"Tool calling OpenAI failed: {openai_error}")

        llm_with_tools = llm_service.fallback_llm.bind_tools(TOOLS)

        response = llm_with_tools.invoke(messages)

        return response
