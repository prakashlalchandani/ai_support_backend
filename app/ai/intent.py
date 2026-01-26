def detect_intent(text: str):
    """
    Detect intent using simple rule-based logic.

    Why rule-based?
    - Transparent
    - Explainable
    - Easy to evolve
    """

    text = text.lower()

    if any(word in text for word in ["refund", "money", "charged", "payment"]):
        return "billing_issue"

    if any(word in text for word in ["error", "crash", "bug", "issue"]):
        return "technical_issue"

    if any(word in text for word in ["thank", "love", "great"]):
        return "positive_feedback"

    return "general_query"


"""
- Intent is about reason, not emotion
- Simple logic beats opaque ML early
"""