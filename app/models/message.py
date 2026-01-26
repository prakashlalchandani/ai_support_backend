from pydantic import BaseModel
from datetime import datetime

class MessageCreate(BaseModel):
    content: str

class MessageResponse(BaseModel):
    id: str
    ticket_id: str
    user_id: str
    content: str
    created_at: datetime