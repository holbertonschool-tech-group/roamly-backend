# app/routes/reservation_routes.py
from flask import Blueprint, request, jsonify
from app.models.reservation import Reservation
from app.database import db
from datetime import datetime

reservation_bp = Blueprint('reservation_bp', __name__)

@reservation_bp.route('/reservations', methods=['GET'])
def get_reservations():
    reservations = Reservation.query.all()
    return jsonify([{
        'id': reservation.id,
        'user_id': reservation.user_id,
        'hotel_id': reservation.hotel_id,
        'check_in': reservation.check_in,
        'check_out': reservation.check_out
    } for reservation in reservations])

@reservation_bp.route('/reservations', methods=['POST'])
def create_reservation():
    data = request.json
    new_reservation = Reservation(
        user_id=data['user_id'],
        hotel_id=data['hotel_id'],
        check_in=datetime.strptime(data['check_in'], '%Y-%m-%d'),
        check_out=datetime.strptime(data['check_out'], '%Y-%m-%d')
    )
    db.session.add(new_reservation)
    db.session.commit()
    return jsonify({'message': 'Reservation created successfully'}), 201
