from transformers import pipeline

def sentimental_analysis(token,positive,negative,neutral,relevance):
    analyser=pipeline('sentiment-analysis')
    sentiment=[analyser(token)][0][0]['label']
    if sentiment=='POSITIVE':
        positive[relevance]=token
    elif sentiment=='NEGATIVE':
        negative[relevance]=token
    else:
        neutral[relevance]=token