from fastapi import (
    APIRouter,
    HTTPException,
)

from schemas.request_schema import ChatRequest

from schemas.response_schema import ChatResponse

from services.logging_service import log_json

from guardrails.security_manager import validate_query

from chains.orchestrator_chain import run_orchestrator

from chains.intent_router_chain import run_intent_chain

router = APIRouter()


@router.post(
    "/chat",
    response_model=ChatResponse,
)
def chat(request: ChatRequest):

    try:

        validation = validate_query(request.query)

        if not validation["allowed"]:

            return ChatResponse(
                intent="blocked",
                sentiment="neutral",
                confidence=1.0,
                escalation_required=False,
                answer=validation["reason"],
            )

        intent_response = run_intent_chain(validation["query"])

        final_answer = run_orchestrator(
            validation["query"],
            request.session_id,
        )

        response = ChatResponse(
            intent=intent_response.intent,
            sentiment=intent_response.sentiment,
            confidence=intent_response.confidence,
            escalation_required=(intent_response.escalation_required),
            answer=final_answer,
        )

        log_json(
            {
                "query": request.query,
                "response": response.model_dump(),
            }
        )

        return response

    except Exception as e:

        log_json({"error": str(e)})

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )
