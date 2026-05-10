from pydantic import BaseModel
from typing import Optional


class EMICalculatorInput(BaseModel):
    principal: float
    annual_rate: float
    tenure_years: int


class CurrencyExchangeInput(BaseModel):
    amount: float
    from_currency: str
    to_currency: str


class ComplaintTriageInput(BaseModel):
    complaint: str
    sentiment: str


class TicketCreationInput(BaseModel):
    customer_query: str
    priority: str
    sentiment: str
    escalation_required: bool
