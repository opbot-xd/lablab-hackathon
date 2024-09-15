import tweepy,os
from dotenv import load_dotenv
load_dotenv()
client=tweepy.Client(
    #bearer_token=os.getenv("BEARER_TOKEN"),
                     consumer_key=os.getenv("API_KEY"),
                     consumer_secret=os.getenv("API_KEY_SECRET"),
                     access_token=os.getenv("ACCESS_TOKEN"),
                     access_token_secret=os.getenv("ACCESS_TOKEN_SECRET"))

def send_tweet(tweet):
    client.create_tweet(text=tweet)
send_tweet("TEST tweet 1")

