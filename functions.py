import json
import logging

from config import POST_PATH
from exceptions import JsonError


def get_logger(name: str, filename: str) -> logging.Logger:
    """Get or create a logger with a file handler"""
    logger = logging.getLogger(name)
    log_formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')

    file_handler = logging.FileHandler(filename, encoding='utf8')
    file_handler.setFormatter(log_formatter)

    logger.addHandler(file_handler)
    logger.setLevel(logging.INFO)
    return logger


def load_json(filename: str) -> list | dict:
    """Загружает данные из JSON-файла"""
    try:
        with open(filename, encoding='utf8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        raise JsonError(f'Cannot load JSON file: {e}')


def write_json(data: list | dict, filname: str) -> None:
    """Записывает данные в JSON-файл, перезаписывая содержимое"""
    with open(filname, 'w', encoding='utf8') as f:
        json.dump(data, f, ensure_ascii=False)


def get_posts_all() -> list[dict]:
    posts = load_json(POST_PATH)
    return posts


def search_for_posts(query: str) -> list[dict]:
    posts = get_posts_all()
    result = []
    for post in posts:
        if query.lower() in post['content'].lower():
            result.append(post)
    return result
