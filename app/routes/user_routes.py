from flask import Blueprint, request, jsonify
from app.models.user import User
from app.database import db

user_bp = Blueprint('user_bp', __name__)

# Get all users
@user_bp.route('/users', methods=['GET'])
def get_users():
    """
    Get all users
    ---
    tags:
      - Users  # This groups this endpoint under 'Users' in Swagger UI
    responses:
      200:
        description: A list of usernames
        schema:
          type: array
          items:
            type: string
    """
    users = User.query.all()
    return jsonify([user.username for user in users])


# Get a user by ID
@user_bp.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    """
    Get a user by ID
    ---
    tags:
      - Users  # This groups this endpoint under 'Users' in Swagger UI
    parameters:
      - in: path
        name: id
        required: true
        schema:
          type: integer
    responses:
      200:
        description: A single user
        schema:
          type: object
          properties:
            id:
              type: integer
            username:
              type: string
            email:
              type: string
      404:
        description: User not found
    """
    user = User.query.get(id)
    if user:
        return jsonify({'id': user.id, 'username': user.username, 'email': user.email})
    return jsonify({'message': 'User not found'}), 404


# Create a new user
@user_bp.route('/users', methods=['POST'])
def create_user():
    """
    Create a new user
    ---
    tags:
      - Users  # This groups this endpoint under 'Users' in Swagger UI
    parameters:
      - in: body
        name: user
        description: The user to create
        schema:
          type: object
          required:
            - username
            - email
            - password
          properties:
            username:
              type: string
            email:
              type: string
            password:
              type: string
    responses:
      201:
        description: User created successfully
      400:
        description: Invalid input
    """
    data = request.json
    new_user = User(username=data['username'], email=data['email'], password=data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201


# Update an existing user
@user_bp.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    """
    Update an existing user
    ---
    tags:
      - Users  # This groups this endpoint under 'Users' in Swagger UI
    parameters:
      - in: path
        name: id
        required: true
        schema:
          type: integer
      - in: body
        name: user
        description: The user data to update
        schema:
          type: object
          properties:
            username:
              type: string
            email:
              type: string
    responses:
      200:
        description: User updated successfully
      404:
        description: User not found
      400:
        description: Invalid input
    """
    data = request.json
    user = User.query.get(id)
    if user:
        user.username = data.get('username', user.username)
        user.email = data.get('email', user.email)
        db.session.commit()
        return jsonify({'message': 'User updated successfully'})
    return jsonify({'message': 'User not found'}), 404


# Delete a user by ID
@user_bp.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    """
    Delete a user by ID
    ---
    tags:
      - Users  # This groups this endpoint under 'Users' in Swagger UI
    parameters:
      - in: path
        name: id
        required: true
        schema:
          type: integer
    responses:
      200:
        description: User deleted successfully
      404:
        description: User not found
    """
    user = User.query.get(id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User deleted successfully'})
    return jsonify({'message': 'User not found'}), 404
