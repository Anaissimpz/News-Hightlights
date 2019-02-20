from app import app
import urllib.request,json
from .models import sources,article
Source = sources.Source
Article = article.Article

# Getting api key
api_key = app.config['NEWS_API_KEY']
# Getting the movie base url
base_url = app.config["NEWS_API_BASE_URL"]
article_base_url= app.config["ARTICLE_API_BASE_URL"]
def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_results(source_results_list)


    return source_results
def process_results(source_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects
    Args:
    movie_list: A list of dictionaries that contain movie details
    Returns :
    movie_results: A list of movie objects
    '''
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('original_name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')
        country= source_item.get('country')

        if url:
            source_object = Source(id,name,description,url,category,language,country)
            source_results.append(source_object)

    return source_results
def get_article(id):
    '''
    Function that gets the json response to our url request
    '''
    get_article_url = article_base_url.format(id,api_key)

    with urllib.request.urlopen(get_article_url) as url:
        get_article_data = url.read()
        get_article_response = json.loads(get_article_data)

        article_results = None
        if get_article_response['articles']:
            article_results_list = get_article_response['articles']
            article_results = process_results(article_results_list)
    return article_results

def process_results(article_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects
    Args:
    movie_list: A list of dictionaries that contain movie details
    Returns :
    movie_results: A list of movie objects
    '''
    article_results = []
    for article_item in article_list:
        id = article_item.get('id')
        author = article_item.get('author')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')
        content= article_item.get('content')

        if url:
            article_object = Article(id,author,description,url,urlToImage,publishedAt,content)
            article_results.append(article_object)

    return article_results