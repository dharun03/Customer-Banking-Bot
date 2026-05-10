from langchain_core.tools import tool

from langchain_core.prompts import ChatPromptTemplate

from langchain_core.output_parsers import PydanticOutputParser

from services.llm_service import llm

from schemas.complaint_triage_schema import ComplaintTriageResponse

from prompts.complaint_triage_prompt import COMPLAINT_TRIAGE_PROMPT

parser = PydanticOutputParser(pydantic_object=ComplaintTriageResponse)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", COMPLAINT_TRIAGE_PROMPT),
        (
            "human",
            """
Complaint:
{complaint}

Customer Sentiment:
{sentiment}

{format_instructions}
""",
        ),
    ]
).partial(format_instructions=parser.get_format_instructions())

chain = prompt | llm | parser


@tool
def complaint_triage_tool(
    complaint: str,
    sentiment: str,
):
    """
    Analyze banking complaint severity
    and assign enterprise priority.
    """

    response = chain.invoke(
        {
            "complaint": complaint,
            "sentiment": sentiment,
        }
    )

    return response.model_dump()
