from langchain_core.prompts import ChatPromptTemplate

from langchain_core.output_parsers import (
    PydanticOutputParser,
)

from services.llm_service import llm_service

from prompts.guardrails import (
    GUARDRAIL_SYSTEM_PROMPT,
)

from schemas.guardrail_schema import (
    GuardrailResponse,
)

parser = PydanticOutputParser(pydantic_object=GuardrailResponse)


def run_guardrail_chain(query: str):

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", GUARDRAIL_SYSTEM_PROMPT),
            (
                "human",
                """
User Query:
{query}

{format_instructions}
""",
            ),
        ]
    ).partial(format_instructions=parser.get_format_instructions())

    formatted_prompt = prompt.format_messages(
        query=query,
    )

    response = llm_service.invoke(formatted_prompt)

    parsed_response = parser.parse(response.content)

    return parsed_response
