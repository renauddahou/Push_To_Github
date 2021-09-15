import tweepy 
consumer_key = 'tx75v4aD7qk81A5rfiITGWhRm'
secret_key = 'mJ3OJ7YG36XmX7Twk06yMv8XcoG6PkAf2DNW2pusIofbJdrm8a'
access_token = "343351837-RDEgyiJZnW1RmkzrJB7TAhUs2iI6eBd7APG18COc"
token_secret = "cXc2RCv7pzpvhOjrTOZyjDG3kCeLbgaK62iwuPpSsInhv"
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