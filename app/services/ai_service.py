from datetime import datetime
from app.ai.sentiment import analyze_sentiment
from app.ai.intent import detect_intent
from app.ai.priority import decide_priority
from app.services.db_collections import ai_results_collection
from app.services.db_collections import tickets_collection
from bson import ObjectId

def analyze_message(message_id: str, content: str, ticket_id: str):
    """
    Run AI analysis on a message and store results.

    Why service:
    - Keeps routes clean
    - Central AI pipeline
    """

    sentiment = analyze_sentiment(content)
    intent = detect_intent(content)

    priority = decide_priority(
        sentiment = sentiment["label"],
        sentiment_score = sentiment["score"],
        intent = intent
    )

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

    # update ticket priority
    tickets_collection.update_one(
        {"_id": ObjectId(ticket_id)},
        {
            "$set": {
                "priority": priority,
                "updated_at": datetime.utcnow()
            }
        }
    )

    return ai_result


# 📌 Learning:

# AI suggests, system applies

# Priority is updated centrally

# This can be logged, reverted, or audited