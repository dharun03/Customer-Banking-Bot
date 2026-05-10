from langchain_core.messages import (
    HumanMessage,
    SystemMessage,
)

from services.llm_service import llm

from tools.tools_registry import TOOLS

from prompts.agent_prompt import AGENT_SYSTEM_PROMPT

llm_with_tools = llm.bind_tools(TOOLS)


def run_tool_calling_chain(
    query: str,
    memory_messages: list,
):

    messages = [
        SystemMessage(content=AGENT_SYSTEM_PROMPT),
        *memory_messages,
        HumanMessage(content=query),
    ]

    response = llm_with_tools.invoke(messages)

    return response
