from fastapi import APIRouter

from memory.session_store import SESSION_STORE

router = APIRouter()


@router.post("/reset/{session_id}")
def reset_memory(
    session_id: str,
):

    if session_id in SESSION_STORE:

        del SESSION_STORE[session_id]

    return {"message": "Memory reset successful"}
