import logging

from flask import Blueprint, render_template, request
from functions import search_for_posts, get_logger
from config import LOG_PATH

main_blueprint = Blueprint('main_blueprint', __name__)

logger = logging.getLogger('main')


@main_blueprint.get('/')
def page_index():
    return render_template('index.html')


@main_blueprint.get('/search')
def page_search():
    query = request.args.get('s')
    if query:
        posts_found = search_for_posts(query)
        logger.info(f'Выполнен поиск: "{query}"')
        return render_template('post_list.html', posts=posts_found, query=query)
    return render_template('post_list.html')
