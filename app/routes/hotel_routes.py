from flask import Blueprint, request, jsonify
from app.models.hotel import Hotel
from app.database import db

hotel_bp = Blueprint('hotel_bp', __name__)

# Get all hotels
@hotel_bp.route('/hotels', methods=['GET'])
def get_hotels():
    """
    Get all hotels
    ---
    tags:
      - Hotels  # Group under 'Hotels' in Swagger UI
    responses:
      200:
        description: A list of hotel names
        schema:
          type: array
          items:
            type: string
    """
    hotels = Hotel.query.all()
    return jsonify([hotel.name for hotel in hotels])

# Create a new hotel
@hotel_bp.route('/hotels', methods=['POST'])
def create_hotel():
    """
    Create a new hotel
    ---
    tags:
      - Hotels  # Group under 'Hotels' in Swagger UI
    parameters:
      - in: body
        name: hotel
        description: The hotel to create
        schema:
          type: object
          required:
            - name
            - destination_id
          properties:
            name:
              type: string
            destination_id:
              type: integer
    responses:
      201:
        description: Hotel created successfully
      400:
        description: Invalid input
    """
    data = request.json
    new_hotel = Hotel(name=data['name'], destination_id=data['destination_id'])
    db.session.add(new_hotel)
    db.session.commit()
    return jsonify({'message': 'Hotel created successfully'}), 201

# Get a hotel by ID
@hotel_bp.route('/hotels/<int:id>', methods=['GET'])
def get_hotel(id):
    """
    Get a hotel by ID
    ---
    tags:
      - Hotels  # Group under 'Hotels' in Swagger UI
    parameters:
      - in: path
        name: id
        required: true
        schema:
          type: integer
    responses:
      200:
        description: A single hotel
        schema:
          type: object
          properties:
            id:
              type: integer
            name:
              type: string
            destination_id:
              type: integer
      404:
        description: Hotel not found
    """
    hotel = Hotel.query.get(id)
    if hotel:
        return jsonify({'id': hotel.id, 'name': hotel.name, 'destination_id': hotel.destination_id})
    return jsonify({'message': 'Hotel not found'}), 404

# Update an existing hotel
@hotel_bp.route('/hotels/<int:id>', methods=['PUT'])
def update_hotel(id):
    """
    Update an existing hotel
    ---
    tags:
      - Hotels  # Group under 'Hotels' in Swagger UI
    parameters:
      - in: path
        name: id
        required: true
        schema:
          type: integer
      - in: body
        name: hotel
        description: The hotel data to update
        schema:
          type: object
          properties:
            name:
              type: string
            destination_id:
              type: integer
    responses:
      200:
        description: Hotel updated successfully
      404:
        description: Hotel not found
      400:
        description: Invalid input
    """
    data = request.json
    hotel = Hotel.query.get(id)
    if hotel:
        hotel.name = data.get('name', hotel.name)
        hotel.destination_id = data.get('destination_id', hotel.destination_id)
        db.session.commit()
        return jsonify({'message': 'Hotel updated successfully'})
    return jsonify({'message': 'Hotel not found'}), 404

# Delete a hotel by ID
@hotel_bp.route('/hotels/<int:id>', methods=['DELETE'])
def delete_hotel(id):
    """
    Delete a hotel by ID
    ---
    tags:
      - Hotels  # Group under 'Hotels' in Swagger UI
    parameters:
      - in: path
        name: id
        required: true
        schema:
          type: integer
    responses:
      200:
        description: Hotel deleted successfully
      404:
        description: Hotel not found
    """
    hotel = Hotel.query.get(id)
    if hotel:
        db.session.delete(hotel)
        db.session.commit()
        return jsonify({'message': 'Hotel deleted successfully'})
    return jsonify({'message': 'Hotel not found'}), 404

