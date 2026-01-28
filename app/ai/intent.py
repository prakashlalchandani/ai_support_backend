def detect_intent(text: str) -> str:
    text = text.lower()

    if any(word in text for word in ["refund", "money back", "return"]):
        return "refund"

    if any(word in text for word in ["complaint", "bad", "worst", "angry"]):
        return "complaint"

    if any(word in text for word in ["how", "what", "why", "help"]):
        return "query"

    if any(word in text for word in ["thanks", "great", "good", "awesome"]):
        return "feedback"

    # 🔥 GUARANTEED FALLBACK
    return "general"
