from app import app
import urllib.request,json
from .models import news_source

NewsSource = news_source.NewsSource

# Getting api key
api_key = app.config["NEWS_API_KEY"]

# Getting the news base url
base_url = app.config["BASE_NEWS_API_URL"]

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