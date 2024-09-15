from data_processing import process_data
from generate_tweet import generate_tweet
from scrape import scrape_tweet
from sentimental_analysis import sentimental_analysis

def script(query,mood):
    tweets=scrape_tweet(query)
    print("these are the tweets",tweets)
    collections = {
        "positive": {},
        "negative": {},
        "neutral": {}
    }
    for tweet in tweets:
        tokens=process_data(tweet[0])
        for i in range(len(tokens)):
            sentiment=sentimental_analysis(tokens[i])
            if sentiment=='POSITIVE':
                collections['positive'][i]=tokens[i]
            elif sentiment=='NEGATIVE':
                collections['negative'][i]=tokens[i]
            else:
                collections['neutral'][i]=tokens[i]

    generated_tweet=generate_tweet(mood,collections[mood],query)
    print("This is the generated tweet",generated_tweet)

script("Education in India","negative")