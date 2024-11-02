import requests
import os
from dotenv import load_dotenv

def give_news(user_input):
    load_dotenv()
    NEWS_KEY = os.getenv("NEWS_KEY")
    url = ('https://newsapi.org/v2/top-headlines?'
        'q='+str(user_input)+'&'
        'sortBy=popularity&'
        'pageSize=5&'
        'apiKey='+str(NEWS_KEY))

    response = requests.get(url)
    json = response.json()
    news = []
        
    for article in json["articles"]:
        if article['source']['id'] != None:
            article_info = {
                "title": article.get("title"),
                "author": article.get("author"),
                "description": article.get("description"),
                "published_date": article.get("publishedAt"),
                "content": article.get("content")
            }
            news.append(article_info)
    return news