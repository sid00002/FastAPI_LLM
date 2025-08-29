from fastapi import FastAPI
from app.api.v1 import health

app = FastAPI(
    title= "LLM Project",
    version= "1.0.0"
)

app.include_router(health.router, prefix="/api/v1/health", tags=["Health"])

