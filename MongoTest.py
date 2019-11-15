import pymongo

from pymongo import MongoClient

examination_id = 11
client = MongoClient()

db = client.twitterData

users = db.twitterUsers
# users.create_index([("screen_name", pymongo.)])

mydict = {"screen_name": "John", "processed": False, "examination_id": examination_id}
#
x = users.insert_one(mydict)

print(x.inserted_id)

xxx = users.find_one({"examination_id": examination_id, "screen_name": "John"})

print(xxx['_id'])

users.delete_one({"examination_id": examination_id, "screen_name": "John"})
# not_proceeded_users = users.find({"examination_id": examination_id, "processed": False})
#
#
# for user in not_proceeded_users:
#     users.update_one({"_id": user["_id"]}, {"$set": {"processed": True}})
#
#
# twits = db.users_twits




