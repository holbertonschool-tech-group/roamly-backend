from flask import Blueprint, request, jsonify
from flasgger import swag_from
from app.service.user_service import UserService

# Blueprint yaradılır
user_bp = Blueprint('users', __name__, url_prefix='/api/users')

# 1. Get all users
@user_bp.route('/', methods=['GET'])
@swag_from({
    "tags": ["Users"],
    "responses": {
        200: {
            "description": "Get all users",
            "examples": {
                "application/json": [
                    {"id": 1, "username": "john_doe", "email": "john@example.com"}
                ]
            }
        }
    }
})
def get_users():
    """Get all users"""
    users = UserService.get_all_users()
    return jsonify(users), 200

# 2. Create a new user
@user_bp.route('/', methods=['POST'])
@swag_from({
    "tags": ["Users"],
    "parameters": [
        {
            "name": "body",
            "in": "body",
            "required": True,
            "schema": {
                "id": "UserRequestDTO",
                "required": ["username", "email", "password"],
                "properties": {
                    "username": {"type": "string", "example": "john_doe"},
                    "email": {"type": "string", "example": "john@example.com"},
                    "password": {"type": "string", "example": "123456"}
                }
            }
        }
    ],
    "responses": {
        201: {
            "description": "User created successfully",
            "examples": {
                "application/json": {
                    "id": 1,
                    "username": "john_doe",
                    "email": "john@example.com"
                }
            }
        }
    }
})
def create_user():
    """Create a new user"""
    data = request.get_json()
    user = UserService.create_user(data)
    return jsonify(user), 201

# 3. Get user by ID
@user_bp.route('/<int:user_id>', methods=['GET'])
@swag_from({
    "tags": ["Users"],
    "parameters": [
        {
            "name": "user_id",
            "in": "path",
            "type": "integer",
            "required": True,
            "description": "ID of the user to retrieve",
            "example": 1
        }
    ],
    "responses": {
        200: {
            "description": "User found",
            "examples": {
                "application/json": {
                    "id": 1,
                    "username": "john_doe",
                    "email": "john@example.com"
                }
            }
        },
        404: {
            "description": "User not found",
            "examples": {
                "application/json": {"error": "User with ID 1 not found"}
            }
        }
    }
})
def get_user_by_id(user_id):
    """Get user by ID"""
    try:
        user = UserService.get_user_by_id(user_id)
        return jsonify(user), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 404
