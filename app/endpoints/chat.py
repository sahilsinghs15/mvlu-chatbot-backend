from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.langchain_services import get_llm_response

router = APIRouter()

class ChatRequest(BaseModel):
    prompt: str

@router.post("/chat")
def chat(request: ChatRequest):
    try:
        response = get_llm_response(request.prompt)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
