from app.ai.priority_rules import PRIORITY_RULES

def decide_priority(sentiment: str, sentiment_score: float, intent: str):
    """
    Generic rule engine.

    Evaluates rules top-down.
    First matching rule wins.
    """

    for rule in PRIORITY_RULES:
        conditions = rule["conditions"]

        # Check sentiment if required
        if "sentiment" in conditions:
            if sentiment != conditions["sentiment"]:
                continue

        # Check sentiment score threshold if required
        if "max_sentiment_score" in conditions:
            if sentiment_score > conditions["max_sentiment_score"]:
                continue

        # Check intent match if required
        if "intents" in conditions:
            if intent not in conditions["intents"]:
                continue

        return rule["priority"]

    # Default fallback
    return "medium"
