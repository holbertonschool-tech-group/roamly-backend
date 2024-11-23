from app.entity.user import User

class UserDTO:
    @staticmethod
    def from_entity(user):
        return {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "created_at": user.created_at,
            "updated_at": user.updated_at
        }

    @staticmethod
    def to_entity(data):
        return User(
            username=data['username'],
            email=data['email'],
            password=data['password']
        )
