# app/__init__.py
from flask import Flask
from flasgger import Swagger 
from app.database import init_db


from app.routes.user_routes import user_bp
from app.routes.destination_routes import destination_bp
from app.routes.hotel_routes import hotel_bp
from app.routes.reservation_routes import reservation_bp
from app.routes.blog_routes import blog_bp

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://pass:1212@localhost/roamly'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    init_db(app)

    # Register blueprints
    app.register_blueprint(user_bp, url_prefix='/api/users')
    app.register_blueprint(destination_bp, url_prefix='/api/destinations')
    app.register_blueprint(hotel_bp, url_prefix='/api/hotels')
    app.register_blueprint(reservation_bp, url_prefix='/api/reservations')
    app.register_blueprint(blog_bp, url_prefix='/api/blog')

    Swagger(app)


    return app
