from fastapi import APIRouter, Depends
from app.core.dependencies import get_current_user
from app.services.ticket_service import create_ticket

router = APIRouter(prefix="/tickets", tags=["Tickets"])

@router.post("/")
def create_new_ticket(
    priority: str = "medium",
    current_user=Depends(get_current_user)
):

    """
    create new ticket for logged-in user
    learning point:
    - Routes does not know DB details
    - Routes only orchestrates logic
    """

    ticket = create_ticket(
        user_id=str(current_user["_id"]),
        priority=priority
    )

    return {
        "message": "Ticket created successfully",
        "ticket_id": str(ticket["_id"])
    }

    """
    key learning:
    Depends(get_current_user) is a protection
    route is thin, readable and boring
    """

