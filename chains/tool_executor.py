from langchain_core.messages import ToolMessage

from tools.tools_registry import TOOLS

TOOL_MAP = {tool.name: tool for tool in TOOLS}


def execute_tools(response):

    tool_results = []

    if not response.tool_calls:
        return []

    for tool_call in response.tool_calls:

        tool_name = tool_call["name"]

        tool_args = tool_call["args"]

        tool = TOOL_MAP.get(tool_name)

        if not tool:
            continue

        result = tool.invoke(tool_args)

        tool_results.append(
            ToolMessage(
                content=str(result),
                tool_call_id=tool_call["id"],
            )
        )

    return tool_results
