class UserResponseDTO:
    def __init__(self, id, username, email, created_at, updated_at):
        self.id = id
        self.username = username
        self.email = email
        self.created_at = created_at
        self.updated_at = updated_at

    @staticmethod
    def from_entity(user):
        return UserResponseDTO(
            id=user.id,
            username=user.username,
            email=user.email,
            created_at=user.created_at,
            updated_at=user.updated_at
        )

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
