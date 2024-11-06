from flask import Blueprint, request, jsonify
from app.models.reservation import Reservation
from app.database import db
from datetime import datetime

reservation_bp = Blueprint('reservation_bp', __name__)

# Get all reservations
@reservation_bp.route('/reservations', methods=['GET'])
def get_reservations():
    """
    Get all reservations
    ---
    tags:
      - Reservations  # This groups this endpoint under 'Reservations' in Swagger UI
    responses:
      200:
        description: A list of reservations with their details
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
              user_id:
                type: integer
              hotel_id:
                type: integer
              check_in:
                type: string
                format: date
              check_out:
                type: string
                format: date
    """
    reservations = Reservation.query.all()
    return jsonify([{
        'id': reservation.id,
        'user_id': reservation.user_id,
        'hotel_id': reservation.hotel_id,
        'check_in': reservation.check_in,
        'check_out': reservation.check_out
    } for reservation in reservations])


# Create a new reservation
@reservation_bp.route('/reservations', methods=['POST'])
def create_reservation():
    """
    Create a new reservation
    ---
    tags:
      - Reservations  # This groups this endpoint under 'Reservations' in Swagger UI
    parameters:
      - in: body
        name: reservation
        schema:
          type: object
          required:
            - user_id
            - hotel_id
            - check_in
            - check_out
          properties:
            user_id:
              type: integer
            hotel_id:
              type: integer
            check_in:
              type: string
              format: date
            check_out:
              type: string
              format: date
    responses:
      201:
        description: Reservation created successfully
    """
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


# Get a single reservation by ID
@reservation_bp.route('/reservations/<int:id>', methods=['GET'])
def get_reservation(id):
    """
    Get a single reservation by ID
    ---
    tags:
      - Reservations  # This groups this endpoint under 'Reservations' in Swagger UI
    parameters:
      - in: path
        name: id
        type: integer
        required: true
    responses:
      200:
        description: Reservation details
        schema:
          type: object
          properties:
            id:
              type: integer
            user_id:
              type: integer
            hotel_id:
              type: integer
            check_in:
              type: string
              format: date
            check_out:
              type: string
              format: date
      404:
        description: Reservation not found
    """
    reservation = Reservation.query.get(id)
    if not reservation:
        return jsonify({'message': 'Reservation not found'}), 404
    return jsonify({
        'id': reservation.id,
        'user_id': reservation.user_id,
        'hotel_id': reservation.hotel_id,
        'check_in': reservation.check_in,
        'check_out': reservation.check_out
    })


# Update a reservation
@reservation_bp.route('/reservations/<int:id>', methods=['PUT'])
def update_reservation(id):
    """
    Update a reservation
    ---
    tags:
      - Reservations  # This groups this endpoint under 'Reservations' in Swagger UI
    parameters:
      - in: path
        name: id
        type: integer
        required: true
      - in: body
        name: reservation
        schema:
          type: object
          required:
            - user_id
            - hotel_id
            - check_in
            - check_out
          properties:
            user_id:
              type: integer
            hotel_id:
              type: integer
            check_in:
              type: string
              format: date
            check_out:
              type: string
              format: date
    responses:
      200:
        description: Reservation updated successfully
      404:
        description: Reservation not found
    """
    reservation = Reservation.query.get(id)
    if not reservation:
        return jsonify({'message': 'Reservation not found'}), 404

    data = request.json
    reservation.user_id = data['user_id']
    reservation.hotel_id = data['hotel_id']
    reservation.check_in = datetime.strptime(data['check_in'], '%Y-%m-%d')
    reservation.check_out = datetime.strptime(data['check_out'], '%Y-%m-%d')
    
    db.session.commit()
    return jsonify({'message': 'Reservation updated successfully'})


# Delete a reservation
@reservation_bp.route('/reservations/<int:id>', methods=['DELETE'])
def delete_reservation(id):
    """
    Delete a reservation
    ---
    tags:
      - Reservations  # This groups this endpoint under 'Reservations' in Swagger UI
    parameters:
      - in: path
        name: id
        type: integer
        required: true
    responses:
      200:
        description: Reservation deleted successfully
      404:
        description: Reservation not found
    """
    reservation = Reservation.query.get(id)
    if not reservation:
        return jsonify({'message': 'Reservation not found'}), 404
    
    db.session.delete(reservation)
    db.session.commit()
    return jsonify({'message': 'Reservation deleted successfully'})
