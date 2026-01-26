from pydantic import BaseModel
from datetime import datetime

class AIResultResponse(BaseModel):
    sentiment: str
    sentiment_score: float
    intent: str
    processed_at: datetime