import random

from pymongo import MongoClient
import twint

examination_id = 1
client = MongoClient()

db = client.twitterData
users = db.twitterUsers


def get_followers(username: str):
    c = twint.Config()

    twint.output.follows_list = []
    c.Username = username
    c.Limit = 200
    c.Store_object = True

    twint.run.Followers(c)
    print(len(twint.output.follows_list))
    return twint.output.follows_list


def rec(screen_name):
    followers = get_followers(screen_name)
    print("screen_name: {}, followers {}".format(screen_name, followers))

    filtered_followers = []
    followers_id = []

    for follower in followers:

        mongo_follower = users.find_one({"examination_id": examination_id, "screen_name": follower})

        if mongo_follower:
            followers_id.append(mongo_follower['_id'])
        else:
            inserted = insert_user_to_db(follower)
            filtered_followers.append(follower)
            followers_id.append(inserted.inserted_id)

    updated = {"followers_id": followers_id, "followers_processed": True}
    users.update_one({"examination_id": examination_id, "screen_name": screen_name}, {"$set": updated})


def insert_user_to_db(follower):
    follower_to_db = {"screen_name": follower,
                      "followers_processed": False,
                      "twits_processed": False,
                      "examination_id": examination_id
                      }
    return users.insert_one(follower_to_db)


while True:
    try:
        user = users.find_one({"examination_id": examination_id, "followers_processed": False, "followers_lock": False})
        users.update_one({"_id": user["_id"]}, {"$set": {"followers_lock": True}})
        start = user['screen_name']
        rec(start)
    except Exception as e:
        print("Exception: {}".format(e))
