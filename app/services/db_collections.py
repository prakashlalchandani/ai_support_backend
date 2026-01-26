from app.core.database import get_database

db = get_database()

users_collection = db["users"]
messages_collection = db["messages"]
tickets_collection = db["tickets"]
ai_results_collection = db["ai_results"]
