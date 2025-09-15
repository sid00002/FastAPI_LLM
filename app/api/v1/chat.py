from fastapi import APIRouter
from pydantic import BaseModel
from app.services.llm_service import generate_response

router = APIRouter()

class PromptRequest(BaseModel):
    prompt: str


@router.post("/chat", tags=["LLM"])
async def chat_with_llm(request: PromptRequest):
    """
    API endpoint to interact with Hugging Face model
    """
    reply = await generate_response(request.prompt)
    return {"prompt": request.prompt, "response": reply}
