from fastapi import FastAPI
from app.api.v1 import health

app = FastAPI(
    title= "FastAPI LLM Project",
    version= "1.0.0",
    description="An advanced FastAPI project with LLM and cloud integration"
)

app.include_router(health.router, prefix="/api/v1/health", tags=["Health"])

