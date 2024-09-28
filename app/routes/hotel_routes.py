# app/routes/hotel_routes.py
from flask import Blueprint, request, jsonify
from app.models.hotel import Hotel
from app.database import db

hotel_bp = Blueprint('hotel_bp', __name__)

@hotel_bp.route('/hotels', methods=['GET'])
def get_hotels():
    hotels = Hotel.query.all()
    return jsonify([hotel.name for hotel in hotels])

@hotel_bp.route('/hotels', methods=['POST'])
def create_hotel():
    data = request.json
    new_hotel = Hotel(name=data['name'], destination_id=data['destination_id'])
    db.session.add(new_hotel)
    db.session.commit()
    return jsonify({'message': 'Hotel created successfully'}), 201
