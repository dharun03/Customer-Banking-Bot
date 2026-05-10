from langchain_core.prompts import ChatPromptTemplate

from langchain_core.output_parsers import PydanticOutputParser

from services.llm_service import llm_service

from schemas.response_schema import ChatResponse

from prompts.system_prompts import INTENT_ROUTER_SYSTEM_PROMPT

from vectorstore.retriever import retrieve_examples

from prompts.few_shot_formatter import format_examples

parser = PydanticOutputParser(pydantic_object=ChatResponse)


def run_intent_chain(query: str):

    examples = retrieve_examples(query)

    formatted_examples = format_examples(examples)

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", INTENT_ROUTER_SYSTEM_PROMPT),
            (
                "human",
                """
Relevant Examples:
{examples}

User Query:
{query}

{format_instructions}
""",
            ),
        ]
    ).partial(format_instructions=parser.get_format_instructions())

    formatted_prompt = prompt.format_messages(
        query=query,
        examples=formatted_examples,
    )

    response = llm_service.invoke(formatted_prompt)

    parsed_response = parser.parse(response.content)

    return parsed_response
