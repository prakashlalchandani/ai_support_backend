from fastapi import APIRouter, Depends
from datetime import datetime, timedelta
from app.services.db_collections import ai_results_collection, tickets_collection
from app.core.dependencies import get_current_user

router = APIRouter(prefix="/analytics", tags=["Analytics"])


@router.get("/sentiment/daily")
def daily_sentiment_stats(
    days: int = 7,
    current_user=Depends(get_current_user)
):
    """
    Returns daily sentiment distribution for the last N days.
    """

    start_date = datetime.utcnow() - timedelta(days=days)

    pipeline = [
        {"$match": {"processed_at": {"$gte": start_date}}},
        {
            "$group": {
                "_id": {
                    "date": {"$dateToString": {"format": "%Y-%m-%d", "date": "$processed_at"}},
                    "sentiment": "$sentiment"
                },
                "count": {"$sum": 1}
            }
        },
        {
            "$group": {
                "_id": "$_id.date",
                "sentiments": {
                    "$push": {
                        "sentiment": "$_id.sentiment",
                        "count": "$count"
                    }
                }
            }
        },
        {"$sort": {"_id": 1}}
    ]

    return list(ai_results_collection.aggregate(pipeline))


@router.get("/high-risk-tickets")
def high_risk_tickets(current_user=Depends(get_current_user)):
    """
    Returns tickets with critical or high priority.
    """

    cursor = tickets_collection.find(
        {"priority": {"$in": ["critical", "high"]}},
        {
            "_id": 1,
            "priority": 1,
            "intent": 1,
            "updated_at": 1
        }
    )

    result = []
    for ticket in cursor:
        ticket["_id"] = str(ticket["_id"])  # 🔥 FIX
        result.append(ticket)

    return result



@router.get("/common-intents")
def common_intents(
    days: int = 30,
    current_user=Depends(get_current_user)
):
    """
    Returns most common intents in the last N days.
    """

    start_date = datetime.utcnow() - timedelta(days=days)

    pipeline = [
        {"$match": {"processed_at": {"$gte": start_date}}},
        {
            "$group": {
                "_id": "$intent",
                "count": {"$sum": 1}
            }
        },
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]

    return list(ai_results_collection.aggregate(pipeline))
