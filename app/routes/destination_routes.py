from flask import Blueprint, request, jsonify
from app.models.destination import Destination
from app.database import db
from flask_restx import Api, Resource, fields  # Added import for fields

# Set up Flask-RESTX
destination_bp = Blueprint('destination_bp', __name__)
api = Api(destination_bp)

# Define a destination model for Swagger UI
destination_model = api.model('Destination', {
    'id': fields.Integer(readonly=True, description='The destination unique identifier'),
    'name': fields.String(required=True, description='The name of the destination'),
    'description': fields.String(required=True, description='A description of the destination')
})

@destination_bp.route('/destinations', methods=['GET'])
def get_destinations():
    """
    Get all destinations
    ---
    tags:
      - Destination
    responses:
      200:
        description: A list of destinations
        content:
          application/json:
            schema:
              type: array
              items:
                $ref: '#/components/schemas/Destination'
    """
    destinations = Destination.query.all()
    return jsonify([{
        'id': destination.id,
        'name': destination.name,
        'description': destination.description
    } for destination in destinations])

@destination_bp.route('/destinations/<int:id>', methods=['GET'])
def get_destination(id):
    """
    Get a specific destination by ID
    ---
    tags:
      - Destination
    parameters:
      - in: path
        name: id
        required: true
        type: integer
    responses:
      200:
        description: A single destination
        schema:
          $ref: '#/definitions/Destination'
      404:
        description: Destination not found
    """
    destination = Destination.query.get(id)
    if destination:
        return jsonify({
            'id': destination.id,
            'name': destination.name,
            'description': destination.description
        })
    return jsonify({'message': 'Destination not found'}), 404

@destination_bp.route('/destinations', methods=['POST'])
def create_destination():
    """
    Create a new destination
    ---
    tags:
      - Destination
    parameters:
      - in: body
        name: destination
        description: The destination to create
        schema:
          $ref: '#/definitions/Destination'
    responses:
      201:
        description: Destination created successfully
      400:
        description: Invalid input
    """
    data = request.json
    new_destination = Destination(
        name=data['name'], description=data['description']
    )
    db.session.add(new_destination)
    db.session.commit()
    return jsonify({'message': 'Destination created successfully'}), 201

@destination_bp.route('/destinations/<int:id>', methods=['PUT'])
def update_destination(id):
    """
    Update an existing destination
    ---
    tags:
      - Destination
    parameters:
      - in: path
        name: id
        required: true
        type: integer
      - in: body
        name: destination
        description: The destination data to update
        schema:
          $ref: '#/definitions/Destination'
    responses:
      200:
        description: Destination updated successfully
      404:
        description: Destination not found
      400:
        description: Invalid input
    """
    data = request.json
    destination = Destination.query.get(id)
    if destination:
        destination.name = data.get('name', destination.name)
        destination.description = data.get('description', destination.description)
        db.session.commit()
        return jsonify({'message': 'Destination updated successfully'})
    return jsonify({'message': 'Destination not found'}), 404

@destination_bp.route('/destinations/<int:id>', methods=['DELETE'])
def delete_destination(id):
    """
    Delete a destination by ID
    ---
    tags:
      - Destination
    parameters:
      - in: path
        name: id
        required: true
        type: integer
    responses:
      200:
        description: Destination deleted successfully
      404:
        description: Destination not found
    """
    destination = Destination.query.get(id)
    if destination:
        db.session.delete(destination)
        db.session.commit()
        return jsonify({'message': 'Destination deleted successfully'})
    return jsonify({'message': 'Destination not found'}), 404