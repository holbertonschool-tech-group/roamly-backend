class UserRequestDTO:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    @staticmethod
    def from_json(data):
        return UserRequestDTO(
            username=data['username'],
            email=data['email'],
            password=data['password']
        )
