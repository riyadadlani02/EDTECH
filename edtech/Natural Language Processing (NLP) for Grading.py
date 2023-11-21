import nltk
from nltk.tokenize import word_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

def nlp_based_grading(student_answer):

    sid = SentimentIntensityAnalyzer()
    sentiment_score = sid.polarity_scores(student_answer)
    return sentiment_score['compound']