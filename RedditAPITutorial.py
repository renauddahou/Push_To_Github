import praw #module that had to be imported
reddit = praw.Reddit(client_id='u88rn-ltsha5IA', client_secret='#SECRET', username='CathyBikesBook',
password='#PASSWORD', user_agent='redditapitutorial')
sub_reddit = reddit.subreddit('Python') #'Python' is one of many subreddits on Reddit
print(sub_reddit.display_name)
print(20*"-")
hot_python = sub_reddit.hot(limit=10) #'hot' is one of the subsections 
for submission in hot_python:
    print(submission.title)
    print(submission.url)
