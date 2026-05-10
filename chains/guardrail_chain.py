from langchain_core.prompts import ChatPromptTemplate

from langchain_core.output_parsers import PydanticOutputParser

from services.llm_service import llm

from prompts.guardrails import GUARDRAIL_SYSTEM_PROMPT

from schemas.guardrail_schema import GuardrailResponse

parser = PydanticOutputParser(pydantic_object=GuardrailResponse)

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

guardrail_chain = prompt | llm | parser
