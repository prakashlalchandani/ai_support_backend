from fastapi import APIRouter, Depends, HTTPException
from app.core.dependencies import get_current_user
from app.services.analytics_service import (
    ticket_count_by_priority,
    ticket_count_by_intent,
    message_sentiment_distribution
)

router = APIRouter(prefix="/admin", tags=["Admin"])

def require_admin(user=Depends(get_current_user)):
    """
    Simple admin guard.

    Why:
    - Analytics are sensitive
    - Normal users should not see system-wide data
    """

    if user.get("role") != "admin":
        raise HTTPException(status_code=403, detail="Admin access required")

    return user


@router.get("/ticket-priority")
def tickets_by_priority(admin=Depends(require_admin)):
    return ticket_count_by_priority()


@router.get("/ticket-intent")
def tickets_by_intent(admin=Depends(require_admin)):
    return ticket_count_by_intent()


@router.get("/sentiment-overview")
def sentiment_overview(admin=Depends(require_admin)):
    return message_sentiment_distribution()
