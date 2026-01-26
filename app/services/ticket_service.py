from datetime import datetime
from bson import ObjectId
from app.services.db_collections import tickets_collection

def create_ticket(
    user_id: str,
    priority: str = "medium"
):
    """
    create new support ticket for user

    why this exists:
    - keep db logic out of api routes
    - makes logic reusable
    - easier to test
    """

    ticket = {
        "user_id": ObjectId(user_id),
        "status": "open",
        "priority": priority,
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow()
    }

    result = tickets_collection.insert_one(ticket)

    return ticket

    """
    key learning:
    IDs are created by DB
    timestamps are server responsibility
    services return raw data, not http response
    """