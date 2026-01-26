from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Create analyzer once (reused for all calls)
analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(text: str):
    """
    Analyze sentiment using VADER.

    Returns:
    - sentiment label: positive / neutral / negative
    - sentiment score: compound score (-1 to +1)

    Why VADER:
    - Tuned for human language
    - Handles emphasis, punctuation, capitalization
    - Better than TextBlob for support messages
    """

    scores = analyzer.polarity_scores(text)
    compound = scores["compound"]

    if compound >= 0.5:
        label = "positive"
    elif compound <= -0.5:
        label = "negative"
    else:
        label = "neutral"

    return {
        "label": label,
        "score": compound
    }
