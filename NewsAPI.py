import requests
def getNews():
    api_key = "2a8be1d6f9764cdeadf7f51ab2fd0597"
    url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=2a8be1d6f9764cdeadf7f51ab2fd0597"
    news = requests.get(url).json()
    articles = news["articles"]
    my_articles = []
    my_news = " "
    for article in articles:
        my_articles.append(article["title"])
    for i in range(10):
        my_news = my_news + my_articles[i] + "\n"
    print(my_news)
getNews()