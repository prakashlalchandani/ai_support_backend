from fastapi import APIRouter, Depends, HTTPException
from app.core.dependencies import get_current_user
from app.services.message_service import add_message_for_ticket
from app.services.db_collections import tickets_collection
from bson import ObjectId

router = APIRouter(prefix="/messages", tags=["Messages"])

@router.post("/{ticket_id}")
def add_message(
    ticket_id: str,
    content: str,
    current_user=Depends(get_current_user)
):

    """
    Add a message to a ticket.

    Learning:
    - Validate ownership
    - Never trust client blindly
    """

    ticket = tickets_collection.find_one({"_id": ObjectId(ticket_id)})

    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")

    if ticket["user_id"] != current_user["_id"]:
        raise HTTPException(status_code=403, detail="Not Allowed")

    message = add_message_for_ticket(
        ticket_id=ticket_id,
        user_id=str(current_user["_id"]),
        content=content
    )

    return {
        "message": "Message added successfully",
        "message_id": str(message["_id"])
    }

    """
    key learning:
    - ownership checks are authorization
    - this is real backend security logic
    """

    