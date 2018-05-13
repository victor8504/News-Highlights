from flask import render_template
from app import app
from .request import get_sources

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