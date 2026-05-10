from pydantic import BaseModel, Field


class ChatResponse(BaseModel):

    intent: str = Field(..., description="Detected banking intent")

    sentiment: str = Field(..., description="positive, neutral, frustrated, angry")

    confidence: float = Field(..., ge=0, le=1, description="Confidence score")

    escalation_required: bool = Field(
        ..., description="Whether human escalation is needed"
    )

    answer: str = Field(..., description="Final assistant response")
