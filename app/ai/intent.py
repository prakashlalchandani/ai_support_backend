def detect_intent(text: str):
    """
    Detect intent using simple rule-based logic.

    Why rule-based?
    - Transparent
    - Explainable
    - Easy to evolve
    """

    text = text.lower()

    if any(word in text for word in ["refund", "money back", "charged", "payment"]):
        return "refund"

    if any(word in text for word in ["error", "crash", "bug", "not working"]):
        return "complaint"

    if any(word in text for word in ["how", "what", "can i", "help", "tell me", "which", "when", "where", "why"]):
        return "query"

    if any(word in text for word in ["thank", "love", "great", "awesome"]):
        return "feedback"

    return "query"


"""
- Intent is about reason, not emotion
- Simple logic beats opaque ML early
"""