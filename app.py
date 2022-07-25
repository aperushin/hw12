from flask import Flask, send_from_directory

from main.views import main_blueprint
from loader.views import loader_blueprint

from exceptions import JsonError
from functions import get_logger
from config import LOG_PATH

logger = get_logger('main', LOG_PATH)

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024
app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


@app.errorhandler(JsonError)
def json_error(e):
    logger.error(e)
    return 'Ошибка загрузки', 500


if __name__ == '__main__':
    app.run(port=5003)
