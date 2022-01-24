import tweepy 
consumer_key = 'tx75v4aD7qk81A5rfiITGWhRm'
secret_key = '#SECRET KEY'
access_token = "#accesstoken"
token_secret = "SECRET TOKEN"
auth = tweepy.OAuthHandler(consumer_key, secret_key)
auth.set_access_token(access_token, token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)
class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status.user.screen_name + "tweeted: " + status.text)
def streamtweets():
        myStreamListener = MyStreamListener()
        myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
        myStream.filter(track=['cancel culture'])
streamtweets()
