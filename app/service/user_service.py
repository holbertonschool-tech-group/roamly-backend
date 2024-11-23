from app.repository.user_repository import UserRepository
from app.dto.user_dto import UserDTO
from app.exceptions.user_exceptions import UserNotFoundException

class UserService:
    @staticmethod
    def get_all_users():
        users = UserRepository.get_all()
        return [UserDTO.from_entity(user) for user in users]

    @staticmethod
    def get_user_by_id(user_id):
        user = UserRepository.get_by_id(user_id)
        if not user:
            raise UserNotFoundException(f"User with ID {user_id} not found.")
        return UserDTO.from_entity(user)

    @staticmethod
    def create_user(user_data):
        new_user = UserDTO.to_entity(user_data)
        return UserDTO.from_entity(UserRepository.create(new_user))

    @staticmethod
    def update_user(user_id, user_data):
        user = UserRepository.get_by_id(user_id)
        if not user:
            raise UserNotFoundException(f"User with ID {user_id} not found.")
        user.username = user_data['username']
        user.email = user_data['email']
        user.password = user_data['password']
        return UserDTO.from_entity(UserRepository.update(user))

    @staticmethod
    def delete_user(user_id):
        user = UserRepository.get_by_id(user_id)
        if not user:
            raise UserNotFoundException(f"User with ID {user_id} not found.")
        UserRepository.delete(user)
