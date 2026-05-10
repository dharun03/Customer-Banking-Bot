from typing import Optional

from pydantic import BaseModel


class ChatRequest(BaseModel):

    query: str

    session_id: Optional[str] = "default"
