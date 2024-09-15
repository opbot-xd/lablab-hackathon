from transformers import pipeline

def sentimental_analysis(token):
    analyser=pipeline('sentiment-analysis')
    sentiment=[analyser(token)][0][0]['label']
    return sentiment
