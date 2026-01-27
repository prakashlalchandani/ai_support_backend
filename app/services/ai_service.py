from datetime import datetime
from bson import ObjectId

from app.ai.sentiment import analyze_sentiment
from app.ai.intent import detect_intent
from app.ai.priority_engine import decide_priority
from app.services.db_collections import (
    ai_results_collection,
    tickets_collection,
    messages_collection,
)

def analyze_message(message_id: str, content: str, ticket_id: str):
    """
    Run AI analysis on a message and persist results.

    IMPORTANT:
    - Runs inside Celery worker
    - No return value is expected
    - Side-effects (DB writes) are the output
    """

    # 1. Analyze text
    sentiment = analyze_sentiment(content)
    intent = detect_intent(content)

    # 2. Decide priority using rule engine
    priority = decide_priority(
        sentiment=sentiment["label"],
        sentiment_score=sentiment["score"],
        intent=intent
    )

    # 3. Store AI result
    ai_result = {
        "message_id": ObjectId(message_id),
        "ticket_id": ObjectId(ticket_id),
        "sentiment": sentiment["label"],
        "sentiment_score": sentiment["score"],
        "intent": intent,
        "suggested_priority": priority,
        "processed_at": datetime.utcnow()
    }

    ai_results_collection.insert_one(ai_result)

    # 4. Update message with intent
    messages_collection.update_one(
        {"_id": ObjectId(message_id)},
        {"$set": {"intent": intent}}
    )

    # 5. Update ticket with priority & intent
    tickets_collection.update_one(
        {"_id": ObjectId(ticket_id)},
        {
            "$set": {
                "priority": priority,
                "intent": intent,
                "updated_at": datetime.utcnow()
            }
        }
    )
