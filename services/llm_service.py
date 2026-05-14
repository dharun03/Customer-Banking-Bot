from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic

from langchain_core.messages import BaseMessage

import os

load_dotenv()


class LLMService:

    def __init__(self):

        self.primary_llm = ChatAnthropic(
            model=os.getenv("ANTHROPIC_MODEL"),
            temperature=float(os.getenv("TEMPERATURE")),
            timeout=30,
            max_retries=2,
        )

        self.fallback_llm = ChatOpenAI(
            model=os.getenv("OPENAI_MODEL_NAME"),
            temperature=float(os.getenv("TEMPERATURE")),
            timeout=30,
            max_retries=2,
        )

    def invoke(
        self,
        messages: list[BaseMessage],
    ):

        try:

            print("Using Claude...")

            response = self.primary_llm.invoke(messages)

            if not response.content:
                raise ValueError("Empty response from OpenAI")

            return response

        except Exception as claude_error:

            print(f"Claude failed: {claude_error}")

            try:

                print("Switching to OpenAI fallback...")

                response = self.fallback_llm.invoke(messages)

                if not response.content:
                    raise ValueError("Empty response from Openai")

                return response

            except Exception as openai_error:

                print(f"Claude fallback failed: {openai_error}")

                raise Exception("Both OpenAI and Claude failed.")


llm_service = LLMService()
