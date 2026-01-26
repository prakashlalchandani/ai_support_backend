from datetime import datetime
from bson import ObjectId
from app.services.ai_service import analyze_message
from app.services.db_collections import messages_collection

def add_message_for_ticket(
    ticket_id: str,
    user_id: str,
    content: str
):

    """
    add message for existing ticket
    why separate service:
    - Message will later trigger AI
    - keeps logic reusable
    """

    message = {
        "ticket_id": ObjectId(ticket_id),
        "user_id": ObjectId(user_id),
        "content": content,
        "created_at": datetime.utcnow()
    }


    result = messages_collection.insert_one(message)
    message["_id"] = result.inserted_id

    analyze_message(
        message_id=str(message["_id"]),
        content=content,
        ticket_id=ticket_id
    )

    return message

    """
    key learning:
    Messages are immutable (no update)
    this is where AI hooks later
    """