from fastapi import APIRouter, Depends
from app.services.llm import GenAIService
from pydantic import BaseModel

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest, service: GenAIService = Depends()):
    response_text = await service.generate(request.message)
    return ChatResponse(response=response_text)
