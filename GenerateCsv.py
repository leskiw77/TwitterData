from pymongo import MongoClient

examination_id = 11
client = MongoClient()

db = client.twitterData

users = db.twitterUsers

processed_users = users = users.find({"examination_id": 1, "followers_processed": True})

i = 1
with open("processed_users.csv", "x") as f:
    for u in processed_users:
        i += 1
        if i % 1000 == 0:
            print("Save {} users".format(i))
        x = [str(f) for f in u['followers_id']]
        f.write("{};{};{}\n".format(u['_id'], u['screen_name'], ','.join(x)))


# print(xxx['_id'])

# not_proceeded_users = users.find({"examination_id": examination_id, "processed": False})
#
#
# for user in not_proceeded_users:
#     users.update_one({"_id": user["_id"]}, {"$set": {"processed": True}})
#
#
# twits = db.users_twits




