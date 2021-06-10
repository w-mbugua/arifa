from .models import BlogPost
from decouple import config
import requests



api_key = config('NEWS_API_KEY')


def get_news(interest):
    """
    function that gets thejson resonse to our url request
    """
    base_url = f'https://newsapi.org/v2/everything?q={interest}&apiKey={api_key}'

    data = requests.get(base_url)
    resp = data.json()
    print(resp)

    news_results = None
    if resp['articles']:
        news_list = resp['articles']
        news_results = process_results(news_list)
    return news_results


def process_results(news_list):
    """
    function that processes news results into a list of objects
    :param news_list: a list of dictionaries that contain each article details
    :return: a list of news objects
    """
    news_results = []

    for news_item in news_list:
        title = news_item.get('title')
        author = news_item.get('author')
        body = news_item.get('description')
        link = news_item.get('url')
        image_url = news_item.get('urlToImage')
        pub_time = news_item.get('publishedAt')

        if image_url:
           
            publish_time = publish_time[:10]

            news_object = BlogPost(title=title, author=author, body=body, link=link, image_url=image_url, pub_time=pub_time)
            news_results.append(news_object)
    return news_results