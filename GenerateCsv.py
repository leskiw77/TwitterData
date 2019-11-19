from pymongo import MongoClient

examination_id = 1
client = MongoClient()

db = client.twitterData

users = db.twitterUsers

print("Query starts")
processed_users = users = users.find({"examination_id": examination_id, "followers_processed": True})
print("Query ends")

i = 1
with open("processed_users.csv", "w") as f:
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




