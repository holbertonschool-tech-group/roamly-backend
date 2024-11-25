import os
from flask import Flask
from app.database import init_db
from app.config.database_config import get_config
from app.config.swagger_config import configure_swagger
from app.controller.user_controller import user_bp
from flask_cors import CORS


def create_app():
    app = Flask(__name__)

    env = os.getenv('FLASK_ENV', 'development')  # Environment variable
    app.config.from_object(get_config(env))  # Load configuration

    init_db(app)

    # Configure Flasgger
    configure_swagger(app)
    CORS(app)


# Register Blueprints
    app.register_blueprint(user_bp)  # Qeydiyyatdan keçirin

    return app
