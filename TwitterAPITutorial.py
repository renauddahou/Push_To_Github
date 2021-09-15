#This tutorial uses Twitter API Version 1. Version 2 is also now available
import tweepy
import sys
def twitter_auth():
    try:
        api_key = 'tx75v4aD7qk81A5rfiITGWhRm'
        secret_key = '#SECRET KEY'
    #bearer_token = 'AAAAAAAAAAAAAAAAAAAAAKKPPQEAAAAAebU80OjXhKdNae4QOwem5bbdxX0%3DXfFI2a6P7CpbeOlfs3qLkzD00rzJ9aOYOvGfBhKSCWRv112yAs'
        access_token = '343351837-RDEgyiJZnW1RmkzrJB7TAhUs2iI6eBd7APG18COc'
        token_secret = '#secret token'
    except KeyError:
        sys.stderr.write("TWIITER_* environment variables not set\n")
        sys.exit(1)
    auth = tweepy.OAuthHandler(api_key, secret_key)
    auth.set_access_token(access_token, token_secret)
    return auth 
def get_twitter_client():
    auth = twitter_auth()
    client = tweepy.API(auth, wait_on_rate_limit=True)
    return client
if __name__ == '__main__':
    user = input("Enter username:  ")
    client = get_twitter_client()
    for status in tweepy.Cursor(client.home_timeline, screen_name=user).items(10):
        print(status.text)
