from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from typing import Optional, Dict, Any
from app.config import settings
from app.agent import OmniChiefAgent

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="OmniChief: Autonomous Virtual Chief of Staff for Nonilion"
)

agent = OmniChiefAgent()

class ChatRequest(BaseModel):
    message: str
    user: Optional[str] = "OfficeMember"
    room_id: Optional[str] = "strategy-war-room"

class ChatResponse(BaseModel):
    status: str
    response: str
    has_artifacts: bool

@app.get("/")
def root():
    return {
        "agent": "OmniChief",
        "role": "Autonomous Chief of Staff & Operations Strategist",
        "platform": "Nonilion.com",
        "status": "Online and Operational",
        "version": settings.VERSION
    }

@app.get("/health")
def health():
    return {"status": "healthy", "service": "omnichief-agent"}

@app.post("/chat", response_model=ChatResponse)
def chat_endpoint(payload: ChatRequest):
    if not payload.message.strip():
        raise HTTPException(status_code=400, detail="Message cannot be empty")
    result = agent.run(payload.message)
    return ChatResponse(**result)

@app.post("/webhook")
async def nonilion_webhook(request: Request):
    """
    Webhook endpoint called by Nonilion Bot API when an office member @mentions or messages OmniChief.
    """
    data = await request.json()
    user_message = data.get("message", {}).get("text", "") or data.get("text", "")
    if not user_message:
        return {"reply": "OmniChief online. Please state your strategic request or challenge."}

    result = agent.run(user_message)
    return {
        "reply": result.get("response", ""),
        "meta": {
            "agent": "OmniChief",
            "format": "multimodal_deliverable",
            "has_artifacts": result.get("has_artifacts", False)
        }
    }
