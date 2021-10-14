import tweepy as tw
import credential
from pymongo import MongoClient

# For authorisation
auth = tw.OAuthHandler(credential.API_key, credential.API_secretkey)
auth.set_access_token(credential.Access_token, credential.Accesss_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

tweets = api.user_timeline(screen_name="@MonseMichael1", count=100, include_rts=False, tweet_mode='extended')
tweetsData = []
for info in tweets:
    status = {
        "ID": str(info.id), "TweetAuthor": info.author.name,
        "TweetText": info.full_text, "DateandTime": info.created_at.strftime("%b %d %Y %H:%M:%S")
    }
    tweetsData.append(status)
client = MongoClient(
    "mongodb+srv://Monse:Monse123@assignment2.lwg3r.mongodb.net/DataMining?ssl=true&ssl_cert_reqs=CERT_NONE")
db = client["DataMining"]
collection = db["twitterdata"]
collection.insert_many(tweetsData)
print(tweetsData)