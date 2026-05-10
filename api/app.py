from fastapi import FastAPI

from api.routes.health import router as health_router
from api.routes.chat import router as chat_router
from api.routes.reset import router as reset_router

app = FastAPI(title="Banking AI Assistant")

app.include_router(health_router)
app.include_router(chat_router)
app.include_router(reset_router)
