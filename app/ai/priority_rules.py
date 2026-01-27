"""
Business-defined priority rules.

This file contains NO logic.
Only configuration.
"""

PRIORITY_RULES = [
    {
        "priority": "critical",
        "conditions": {
            "sentiment": "negative",
            "max_sentiment_score": -0.7,
            "intents": ["complaint", "refund"]
        }
    },
    {
        "priority": "high",
        "conditions": {
            "sentiment": "negative",
            "intents": ["complaint", "technical_issue", "billing_issue"]
        }
    },
    {
        "priority": "medium",
        "conditions": {
            "intents": ["query", "technical_issue"]
        }
    },
    {
        "priority": "low",
        "conditions": {
            "intents": ["feedback"]
        }
    }
]
