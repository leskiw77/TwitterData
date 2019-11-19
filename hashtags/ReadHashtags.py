import csv
from collections import Counter

from bson import ObjectId
from pymongo import MongoClient

examination_id = 1

client = MongoClient()

db = client.twitterData

twits = db.users_twits

with open('clusters.csv') as csv_file:
    reader = csv.reader(csv_file, delimiter=';')
    for row in reader:
        cluster_id = row[0]
        users = [ObjectId(x) for x in row[1].split(',')]

        hashes = []

        for t in twits.find({"user_id": {"$in": users}}):
            hashes += t['hashtags']
        print(Counter(hashes))

