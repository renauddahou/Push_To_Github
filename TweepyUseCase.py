import tweepy 
import time

from tweepy.error import TweepError
consumer_key = 'tx75v4aD7qk81A5rfiITGWhRm'
secret_key = '#SECRET KEY'
access_token = "#Access Token"
token_secret = "#SECRET TOKEN"
auth = tweepy.OAuthHandler(consumer_key, secret_key)
auth.set_access_token(access_token, token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)
#api.update_status("As i tweet from Visual Studio Code, be sure to visit my blog at: www.catherinejwrites.com")
#api.update_status("Well folks, thats all for today. I'll explore more of the Twitter API and Tweepy tommorrow")
#api.update_status("Good morning!I'm tweeting from my coding console again.")
#api.update_status("trying to decide whether i want to create a twitter bot. Hmm")
#screen_name = "@CJB_2014"
#statuses = api.user_timeline(screen_name)
#for status in statuses:
    #print(status.text, end="\n\n")
#api.update_status("Ok. off again until later.")
#api.update_status("Hi! I'm back on the code console for a bit. working on a small sentiment analysis project")
#api.update_status("good morning. Tweeting from visual studio code.")
#screen_name = "driscollis"
#api.create_friendship(screen_name)
#ID = '1263493041769394178'
#api.retweet(ID)
#api.update_status("Tweeting from the console. I'm bored. Think I'll go make some crossiants")
#api.update_status("Tweeting from visual studio code in python. About to go for an adventure")
api.update_status("it is human nature to want to belong. It is human nature to want to feel validated")
