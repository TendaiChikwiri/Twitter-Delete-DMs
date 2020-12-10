import json
import tweepy


# fill in your api credentials, you'll need to apply for a developer account first
credentials = {
	"api-key": ,
	"api-secret-key": ,
	"access-token": ,
	"access-token-secret": ,
}

auth = tweepy.OAuthHandler(credentials["api-key"], credentials["api-secret-key"])
auth.set_access_token(credentials["access-token"], credentials["access-token-secret"])

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")
# you need to download your twitter archive and use the "direct-messages.js" file, it countains all of yur direct messages
with open() as dataFile:
    data = dataFile.read()
    dataDict = json.loads(data)
    for x in dataDict:
        try:
            messageid = x['dmConversation']["messages"][0]['messageCreate']["id"]
            api.destroy_direct_message(messageid)
            print("Message deleted")
        except:
            print("Failed to delete message")
            continue
