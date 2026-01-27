from app.services.db_collections import tickets_collection, ai_results_collection

def ticket_count_by_priority():
    """
    Count how many tickets exist per priority.

    Why this exists:
    - Admins need to see workload severity
    - Priority reflects business urgency
    """

    pipeline = [
        {"$group": {"_id": "$priority", "count": {"$sum": 1}}}
    ]

    results = tickets_collection.aggregate(pipeline)

    return {item["_id"]: item["count"] for item in results}


def ticket_count_by_intent():
    """
    Count tickets by detected intent.

    Why:
    - Shows WHY users are contacting support
    """

    pipeline = [
        {"$group": {"_id": "$intent", "count": {"$sum": 1}}}
    ]

    results = tickets_collection.aggregate(pipeline)

    return {item["_id"]: item["count"] for item in results}


def message_sentiment_distribution():
    """
    Count messages by sentiment.

    Why:
    - Measures user emotional health
    """

    pipeline = [
        {"$group": {"_id": "$sentiment", "count": {"$sum": 1}}}
    ]

    results = ai_results_collection.aggregate(pipeline)

    return {item["_id"]: item["count"] for item in results}
