from ntscraper import Nitter

def scrape_tweet(query):
    scraper = Nitter(log_level=1,skip_instance_check=False)
    results=scraper.get_tweets(query,number=200,language='en')
    tweets=results['tweets']
    tweets.sort(reverse=True, key=lambda x:x['stats']['likes'])
    leaderboard=[]
    cumu_likes=dict()
    freq=dict()
    userwise_text=dict()
    for tweet in tweets:
        if tweet['user']['username'] in freq:
            freq[tweet['user']['username']]+=1
            cumu_likes[tweet['user']['username']]+=tweet['stats']['likes']
            userwise_text[tweet['user']['username']].append(tweet['text'])
        else:
            freq[tweet['user']['username']]=1
            cumu_likes[tweet['user']['username']]=tweet['stats']['likes']
            leaderboard.append(tweet['user']['username'])
            userwise_text[tweet['user']['username']]=[]
            userwise_text[tweet['user']['username']].append(tweet['text'])
    leaderboard.sort(reverse=True,key=lambda x:cumu_likes[x])
    ordered_text=[userwise_text[x] for x in leaderboard]
    return ordered_text
#ordered_text is a LIST OF LIST OF strings ordered by likes ie the first list of list is to have the most imporatnce :)