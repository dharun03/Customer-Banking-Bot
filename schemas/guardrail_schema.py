from pydantic import BaseModel


class GuardrailResponse(BaseModel):

    status: str

    reason: str
