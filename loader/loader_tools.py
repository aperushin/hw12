from functions import load_json, write_json
from config import POST_PATH
from werkzeug.datastructures import FileStorage


def add_post(**kwargs) -> None:
    posts = load_json(POST_PATH)
    posts.append(dict(kwargs))
    write_json(posts, POST_PATH)


def is_picture(file: FileStorage) -> bool:
    allowed_extensions = {'jpg', 'jpeg', 'png', 'gif'}
    file_extension = file.filename.split('.')[-1]
    return file_extension in allowed_extensions


def save_picture(picture: FileStorage) -> str:
    """Save uploaded picture and return path to the saved file"""
    picture_path = './uploads/images/' + picture.filename
    picture.save(picture_path)
    return picture_path
