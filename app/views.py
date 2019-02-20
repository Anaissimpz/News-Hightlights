from flask import render_template
from app import app
from .request import get_sources,get_article


@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    general_sources = get_sources('general')
    business_sources = get_sources('business')
    sports_sources = get_sources('sports')
    health_sources = get_sources('health')
    title = 'Home - Welcome to The best News Review Website Online'
    return render_template('index.html', title = title,general = general_sources,business = business_sources,sports = sports_sources,health = health_sources)
@app.route('/article/<id>')
def article(id):

    '''
    View source page function that returns the source details page and its data
    '''
    articles= get_article(id)
    tittle =f'{id}'
    return render_template('article.html',tittle=tittle,articles = articles)