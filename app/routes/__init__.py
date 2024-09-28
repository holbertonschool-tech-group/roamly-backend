# app/routes/__init__.py
from flask import Blueprint

# Blueprint-lərin qeydiyyatı
user_bp = Blueprint('user_bp', __name__)
destination_bp = Blueprint('destination_bp', __name__)
hotel_bp = Blueprint('hotel_bp', __name__)
reservation_bp = Blueprint('reservation_bp', __name__)
blog_bp = Blueprint('blog_bp', __name__)
