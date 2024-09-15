import urllib.parse,requests,os,tweepy
import snscrape.modules.twitter as snstwitter
import pandas as pd
from dotenv import load_dotenv
load_dotenv()
#replace with user input 
initial_prompt="Indian education system sucks"
##must be less than 500 chars
# auth=tweepy.OAuth1UserHandler(
#     os.getenv("API_KEY"),
#     os.getenv("API_KEY_SECRET"),
#     os.getenv("ACCESS_TOKEN"),
#     os.getenv("ACCESS_TOKEN_SECRET")
# )
# api=tweepy.API(auth)


try:
    scraper=snstwitter.TwitterSearchScraper(initial_prompt)
#    response=requests.get(url,
#    headers={})
#    print(url)
    tweets=[]
    for i,tweet in enumerate(scraper.get_items()):

        tweet_data=[
        tweet.data,
        tweet.id,
        tweet.content,
        tweet.user.username,
        tweet.likeCount,
        tweet.retweetCount
        ]
        tweets.append(tweet_data)
        if i>50:
            break

    #response=api.search_tweets(q=encoded_prompt,lang='en',count=100)
    print(len(tweets))
    print(tweets[0])
    

except Exception as e:
   print("Some error occoured in getting the tweets {e}".format(e=e))


