"""
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener


#consumer key, consumer secret, access token, access secret.
ckey="JUwlrJDma6bE274e3nmBchJQc"
csecret="W5bziwhdWZjUEiHMzY16dNanxsdpuLxcJ7vhizslHgTaiqBf9S"
atoken="1251774870121263104-GppJz4zIc4Z9kKYlLGAmLGNGJV25VV"
asecret="5xJiQ2oUKzRI2L8a86e0HfwlP7SMQaLFk9iTc377WXuBI"

class listener(StreamListener):

    def on_data(self, data):
        print(data)
        return(True)

    def on_error(self, status):
        print (status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["car"])
"""
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sentiment_mod as s

#consumer key, consumer secret, access token, access secret.
ckey="JUwlrJDma6bE274e3nmBchJQc"
csecret="W5bziwhdWZjUEiHMzY16dNanxsdpuLxcJ7vhizslHgTaiqBf9S"
atoken="1251774870121263104-GppJz4zIc4Z9kKYlLGAmLGNGJV25VV"
asecret="5xJiQ2oUKzRI2L8a86e0HfwlP7SMQaLFk9iTc377WXuBI"



class listener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)
        tweet = all_data["text"]
        sentiment_value, confidence = s.sentiment(tweet)
        print(tweet, sentiment_value, confidence)

        if confidence*100 >= 80:
            output = open("twitter-out.txt","a")
            output.write(sentiment_value)
            output.write('\n')
            output.close()

        return True

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["happy"])
