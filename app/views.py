from flask import render_template
from app import app
from .request import get_sources,get_articles

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    
    title = 'The best News-Highlights Website Online'

    general_list = get_sources('us', 'general')
    entertainment_list = get_sources('us', 'entertainment')
    sports_list = get_sources('us', 'sports')
    science_list = get_sources('us', 'science')
    health_list = get_sources('us', 'health')                
    business_list = get_sources('us', 'business')
    technology_list = get_sources('us', 'technology')

    return render_template('index.html', title = title, general = general_list, entertainment = entertainment_list,
                           sports = sports_list, science = science_list, health = health_list, business = business_list,
                           technology=technology_list)

@app.route('/news/<id>')
def news(id):
    '''
    View articles page function that returns the news article page from a highlighted news source.
    '''
    news_args = get_articles(id)
    return render_template('news.html',news=news_args)