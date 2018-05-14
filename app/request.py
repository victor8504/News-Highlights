import urllib.request,json
from .models import NewsSource, NewsArticles

# Getting api key
api_key = None

# Getting the news base url
base_url = None

# Getting the source news url
source_url = None

def configure_request(app):
    global api_key,base_url,source_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['BASE_NEWS_API_URL']
    source_url = app.config['SOURCE_NEWS_URL']
    


def get_sources(country, category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(country, category, api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read() # This is a json response
        get_news_response = json.loads(get_news_data) # json response converted to a Python dictionary

        source_results = None

        if get_news_response['sources']:
            source_results_list = get_news_response['sources']
            source_results = process_sources(source_results_list)

    return source_results

def process_sources(source_list):
    '''
    Function  that processes the news sources and transform them to a list of Objects

    Args:
        source_list: A list of dictionaries that contain news sources

    Returns :
        news_results: A list of news objects
    '''
    news_results = []
    for source_item in source_list:
        id = source_item.get('id')
        print(id)
        name = source_item.get('name')
        print(name)
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        country = source_item.get('country')
        
        if url:
            source_object = NewsSource(id,name,description,url,category,country)
            news_results.append(source_object)

    return news_results

def get_articles(source):
    '''
    Function that gets the json response to our url request
    '''
    get_source_news_url = source_url.format(source, api_key)
        
    with urllib.request.urlopen(get_source_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
       

        news_results = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
           
            news_results = process_articles(news_results_list)

    return news_results

def process_articles(articles_list):
    '''
    Function  that processes the news articles and transform them to a list of Objects

    Args:
        articles_list: A list of dictionaries that contain news articles

    Returns :
        news_results: A list of news objects
    '''
    news_results = []
    for result in articles_list:
        id = result['source'].get('id')
        name = result['source'].get('name')            
        author = result.get('author')
        title = result.get('title')
        description = result.get('description')
        url = result.get('url')
        urlToImage = result.get('urlToImage')
        publishedAt = result.get('publishedAt')

        source_object = NewsArticles(id,name,author,title,description,url,urlToImage,publishedAt)
        print(source_object)
        news_results.append(source_object)

    return news_results