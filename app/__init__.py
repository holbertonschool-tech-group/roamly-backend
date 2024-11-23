import os

from flask import Flask
from app.database import init_db
from app.config.database_config import get_config
from app.controller.user_controller import user_ns
from app.config.swagger_config import configure_swagger  # Flask-RESTx Swagger

def create_app():

    app = Flask(__name__)

    env = os.getenv('FLASK_ENV', 'development')  # Mühit dəyişəni: development, production, testing
    app.config.from_object(get_config(env))  # Konfiqurasiyanı yükləyir

    init_db(app)

    api = configure_swagger(app)

    api.add_namespace(user_ns, path='/api/users')

    return app
