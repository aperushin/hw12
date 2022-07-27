import logging

from flask import Blueprint, render_template, request
from loader.loader_tools import add_post, is_picture, save_picture

loader_blueprint = Blueprint('loader', __name__, template_folder='templates')

logger = logging.getLogger('main')


@loader_blueprint.get('/post')
def page_post_form():
    return render_template('post_form.html')


@loader_blueprint.post('/post')
def page_post_upload():
    post_content = request.form.get('content')
    uploaded_file = request.files.get('picture')

    if not uploaded_file or post_content:
        return 'Ошибка загрузки: прикрепите картинку и введите текст'

    if not is_picture(uploaded_file):
        logger.info(f'Попытка загрузки файла запрещённого типа: "{uploaded_file.filename}"')
        return 'Ошибка загрузки: тип файла не поддерживается'

    saved_picture_path = save_picture(uploaded_file)
    add_post(pic=saved_picture_path, content=post_content)
    return render_template(
        'post_uploaded.html',
        pic=saved_picture_path,
        content=post_content
    )
