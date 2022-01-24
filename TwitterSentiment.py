import tweepy
from textblob import TextBlob
api_key = 'tx75v4aD7qk81A5rfiITGWhRm'
secret_key = '#secret_key'
access_token = '#access_token'
token_secret = '#token_secret'
auth = tweepy.OAuthHandler(api_key, secret_key)
auth.set_access_token(access_token, token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)
search_term = "spotify"
tweet_amount = 200
tweets = tweepy.Cursor(api.search, q=search_term, lang='en').items(tweet_amount)
polarity = 0
positive = 0
neutral = 0
negative = 0
for tweet in tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    tweet_polarity = analysis.polarity
    if tweet_polarity > 0:
        positive += 1
    elif tweet_polarity < 0:
        negative += 1
    else:
        neutral += 1
    polarity += tweet_polarity
print(20*'-')
print(f'Polarity: {polarity}')
print(f'Amount of positive tweets: {positive}')
print(f'Amount of negative tweets: {negative}')
print(f'Amount of neutral tweets: {neutral}')
