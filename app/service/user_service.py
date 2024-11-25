from app.repository.user_repository import UserRepository
from app.dto.user_dto import UserDTO
from app.dto.user_request_dto import UserRequestDTO
from app.dto.user_response_dto import UserResponseDTO
from app.exceptions.user_exceptions import UserNotFoundException

class UserService:
    @staticmethod
    def get_all_users():
        users = UserRepository.get_all()
        return [UserResponseDTO.from_entity(user).to_dict() for user in users]

    @staticmethod
    def get_user_by_id(user_id):
        user = UserRepository.get_by_id(user_id)
        if not user:
            raise UserNotFoundException(f"User with ID {user_id} not found.")
        return UserResponseDTO.from_entity(user).to_dict()

    @staticmethod
    def create_user(user_data):
        user_request_dto = UserRequestDTO.from_json(user_data)
        new_user = UserDTO.to_entity({
            "username": user_request_dto.username,
            "email": user_request_dto.email,
            "password": user_request_dto.password
        })
        created_user = UserRepository.create(new_user)
        return UserResponseDTO.from_entity(created_user).to_dict()

    @staticmethod
    def update_user(user_id, user_data):
        user_request_dto = UserRequestDTO.from_json(user_data)
        user = UserRepository.get_by_id(user_id)
        if not user:
            raise UserNotFoundException(f"User with ID {user_id} not found.")
        user.username = user_request_dto.username
        user.email = user_request_dto.email
        user.password = user_request_dto.password
        updated_user = UserRepository.update(user)
        return UserResponseDTO.from_entity(updated_user).to_dict()

    @staticmethod
    def delete_user(user_id):
        user = UserRepository.get_by_id(user_id)
        if not user:
            raise UserNotFoundException(f"User with ID {user_id} not found.")
        UserRepository.delete(user)
