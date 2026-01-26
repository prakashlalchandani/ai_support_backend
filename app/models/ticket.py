from pydantic import BaseModel
from datetime import datetime

class TicketCreate(BaseModel):
    priority: str
    created_at: datetime
    

class TicketResponse(BaseModel):
    id: str
    status: str
    priority: str
    created_at: datetime
    