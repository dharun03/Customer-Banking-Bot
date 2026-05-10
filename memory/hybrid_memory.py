from langchain_core.messages import (
    HumanMessage,
    AIMessage,
    SystemMessage,
)

from services.llm_service import llm_service

from memory.session_store import SESSION_STORE

WINDOW_SIZE = 8


class HybridMemoryManager:

    def __init__(
        self,
        session_id: str,
    ):

        self.session_id = session_id

        if session_id not in SESSION_STORE:

            SESSION_STORE[session_id] = {
                "recent_messages": [],
                "summary": "",
            }

    def get_memory(self):

        return SESSION_STORE[self.session_id]

    def get_context_messages(self):

        memory = self.get_memory()

        messages = []

        if memory["summary"]:

            messages.append(SystemMessage(content=f"""
Conversation Summary:

{memory['summary']}
"""))

        for msg in memory["recent_messages"]:

            if msg["role"] == "user":

                messages.append(HumanMessage(content=msg["content"]))

            else:

                messages.append(AIMessage(content=msg["content"]))

        return messages

    def save_context(
        self,
        user_query: str,
        assistant_response: str,
    ):

        memory = self.get_memory()

        memory["recent_messages"].append(
            {
                "role": "user",
                "content": user_query,
            }
        )

        memory["recent_messages"].append(
            {
                "role": "assistant",
                "content": assistant_response,
            }
        )

        if len(memory["recent_messages"]) > WINDOW_SIZE * 2:

            old_messages = memory["recent_messages"][:-WINDOW_SIZE]

            summary = self.generate_summary(
                old_messages,
                memory["summary"],
            )

            memory["summary"] = summary

            memory["recent_messages"] = memory["recent_messages"][-WINDOW_SIZE:]

    def generate_summary(
        self,
        old_messages,
        existing_summary,
    ):

        conversation_text = ""

        for msg in old_messages:

            conversation_text += f"{msg['role']}: " f"{msg['content']}\n"

        prompt = f"""
    You are a banking conversation summarizer.

    Existing Summary:
    {existing_summary}

    New Conversation:
    {conversation_text}

    Generate an updated concise summary
    preserving important:
    - banking details
    - EMI discussions
    - complaint workflows
    - ticket IDs
    - customer issues
    - context for follow-up questions
    """

        response = llm_service.invoke([HumanMessage(content=prompt)])

        return response.content
