from twitter_scraper import get_tweets

for tweet in get_tweets('kennethreitz', pages=1):
    print(tweet)
    print(dict(tweet))
    print(tweet['entries']['hashtags'])
