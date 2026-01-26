from app.services.db_collections import (
    users_collection,
    tickets_collection,
    messages_collection,
    ai_results_collection
)

def create_indexes():
    # Users
    users_collection.create_index("email", unique=True)

    # tickets
    tickets_collection.create_index("user_id")
    tickets_collection.create_index("priority")
    tickets_collection.create_index("status")

    # messages
    messages_collection.create_index("ticket_id")
    messages_collection.create_index("user_id")

    # ai results
    ai_results_collection.create_index("message_id")
    ai_results_collection.create_index("sentiment")
       