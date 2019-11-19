from twitter_scraper import get_tweets
from pymongo import MongoClient

examination_id = 1

client = MongoClient()

db = client.twitterData

users = db.twitterUsers
twits = db.users_twits


def collect_twits_for_user(db_id, screen_name):
    print("Processing user: {}".format(screen_name))
    for tweet in get_tweets(screen_name):
        tweet_db = {
            "user_id": db_id,
            "screen_name": screen_name,
            "twitterId": tweet['tweetId'],
            "time": tweet['time'],
            "text": tweet['text'],
            "hashtags": tweet['entries']['hashtags'],
            "urls": tweet['entries']['urls'],
            "replies": tweet['replies'],
            "retweets": tweet['retweets'],
            "likes": tweet['likes'],

        }
        twits.insert_one(tweet_db)


while True:
    proceeded_user = users.find_one(
        {"examination_id": examination_id, "followers_processed": True, "twits_processed": False})
    users.update_one({"_id": proceeded_user["_id"]}, {"$set": {"twits_processed": True}})

    try:
        collect_twits_for_user(proceeded_user['_id'], proceeded_user['screen_name'])
    except Exception as e:
        print("Exception: {}".format(e))
