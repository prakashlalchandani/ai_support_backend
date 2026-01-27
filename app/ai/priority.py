'''def decide_priority(sentiment: str, sentiment_score: float, intent: str):
    """
    Decide ticket priority based on AI signals.

    IMPORTANT:
    - This is rule-based on purpose
    - Every rule is explainable
    - Easy to change without retraining models
    """

    # strong negative sentiment -> urgent attention
    if sentiment == "negative" and sentiment_score <= -0.6:
        return "urgent"

    # technical and billing are more serious
    if intent in ["billing_issue", "technical_issue"]:
        if sentiment == "negative":
            return "high"
        return "medium"

    # positive feedback do not create urgency
    if intent == "positive_feedback":
        return "low"

    return "medium"

'''

# 📌 Learning:
# Rules are business-owned, not AI-owned
# No probabilities hidden
# Deterministic outcome