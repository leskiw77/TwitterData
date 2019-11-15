# https://python-twitter.readthedocs.io/en/latest/models.html
import time

import twitter
from pymongo import MongoClient
from twitter import TwitterError

api = twitter.Api(consumer_key='d8Yr7sGwjJlSKS7Ij89oZJwyd',
                  consumer_secret='oAFqzPQnJiqrxWYqlW6xes0WSUdbb5aPFd1qCHYC2cMKZYaBjk',
                  access_token_key='1001841856794243072-XbKn870ZqWDE7r8WDAk3F6Mzaj31rN',
                  access_token_secret='lo6jJgDYu6piZL1iPjW15rwwvubyZlM5l12qvVb2CMmM0')

print(api.GetFriends())
examination_id = 1
client = MongoClient()

db = client.twitterData

users = db.twitterUsers
# users = db.twitter_users
twits = db.users_twits

user_counter = 0
status_counter = 0


def get_statuses():
    not_proceeded_users = users.find({"examination_id": examination_id, "processed": False})

    global user_counter
    global status_counter
    for user in not_proceeded_users:
        screen_name = user["screen_name"]
        # https://developer.twitter.com/en/docs/tweets/timelines/api-reference/get-statuses-user_timeline
        statuses = api.GetUserTimeline(screen_name=screen_name, count=200)

        user_counter += 1
        last_index = 0
        user_id = 0
        print("Processing user: {}, with {} statuses ".format(screen_name, len(statuses)))
        for s in statuses:
            status_counter += 1

            user_hash = [h.AsDict()['text'] for h in s.hashtags]

            twit = {
                "text": s.text,
                "user_id": s.user.id,
                "screen_name": screen_name,
                "examination_id": examination_id,
                "hashes": user_hash
            }
            twits.insert_one(twit)

            user_id = s.user.id
            if s.id > last_index:
                last_index = s.id

        if last_index > 0 and user_id > 0:
            updated = {"processed": True, "twitter_id": user_id, "last_index": last_index}
            # updated = {"twitter_id": user_id, "last_index": last_index}

        else:
            updated = {"processed": True, "last_index": last_index}

        users.update_one({"_id": user["_id"]}, {"$set": updated})
        print("User {}, Status: {}".format(user_counter, status_counter))


while True:
    try:
        get_statuses()
    except TwitterError as e:
        pass
        # print("Need to wait: {}".format(e))
        # 5 minutes + 1 second
        # time.sleep(60 * 5 + 1)
