from flask_restx import Namespace, Resource
from flask import request
from app.service.user_service import UserService

user_ns = Namespace('users', description='User management operations')

@user_ns.route('/')
class Users(Resource):
    def get(self):
        """Get all users"""
        users = UserService.get_all_users()
        return users, 200

    def post(self):
        """Create a new user"""
        data = request.get_json()
        user = UserService.create_user(data)
        return user, 201


@user_ns.route('/<int:user_id>')
class UserById(Resource):
    def get(self, user_id):
        """Get user by ID"""
        try:
            user = UserService.get_user_by_id(user_id)
            return user, 200
        except Exception as e:
            return {"error": str(e)}, 404

    def put(self, user_id):
        """Update user by ID"""
        data = request.get_json()
        try:
            user = UserService.update_user(user_id, data)
            return user, 200
        except Exception as e:
            return {"error": str(e)}, 404

    def delete(self, user_id):
        """Delete user by ID"""
        try:
            UserService.delete_user(user_id)
            return {"message": "User deleted successfully"}, 200
        except Exception as e:
            return {"error": str(e)}, 404
