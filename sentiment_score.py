from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()


def get_score(message):
    sentiment_score = analyzer.polarity_scores(message)["compound"]
    return 2 * ((sentiment_score * -1) - 0.5)
