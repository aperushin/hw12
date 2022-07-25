import logging

from flask import Blueprint, render_template, request
from loader.loader_tools import add_post, is_picture
from functions import get_logger
from config import LOG_PATH

loader_blueprint = Blueprint('loader', __name__)

logger = logging.getLogger('main')


@loader_blueprint.get('/post')
def page_post_form():
    return render_template('post_form.html')


@loader_blueprint.post('/post')
def page_post_upload():
    post_content = request.form.get('content')
    uploaded_file = request.files.get('picture')
    if is_picture(uploaded_file):
        picture_path = 'uploads/images/' + uploaded_file.filename
        uploaded_file.save(picture_path)
        post_dict = {
            'pic': picture_path,
            'content': post_content
        }
        add_post(post_dict)
        return render_template('post_uploaded.html', post=post_dict)

    logger.info(f'Попытка загрузки файла запрещённого типа: {uploaded_file.filename}')
    return 'Ошибка загрузки'
