import pip
import praw
import datetime as dt
import credential
import certifi
import sqlite3

import _sqlite3

from pymongo import MongoClient

redditAuth = praw.Reddit(client_id=credential.Client_ID, client_secret=credential.Client_SecretID, user_agent=credential.user_agent,
                         username=credential.username, password=credential.Password)

redditdata = []
for post in redditAuth.redditor(credential.username).submissions.top():
    redditPosts = {
        "PostId": post.id,
        "PostAuthor": post.author.name,
        "PostTitle": post.title,
        "PostText": post.selftext,
        "DateandTime": dt.datetime.fromtimestamp(post.created).strftime("%b %d %Y %H:%M:%S"),
        }
    redditdata.append(redditPosts)
client = MongoClient("mongodb+srv://Monse:Monse123@assignment2.lwg3r.mongodb.net/DataMining?ssl=true&ssl_cert_reqs=CERT_NONE")
db = client["DataMining"]
collection = db["redditdata"]
collection.insert_many(redditdata)

print(redditdata)