from pydantic import BaseModel


class ComplaintTriageResponse(BaseModel):

    priority: str

    escalation_required: bool

    reason: str
