from service.user import UserService


class AuthService:
    def __init__(self, user_service: UserService):
        self.user_service = user_service


    def generate_tokens(self, username, password):
        user = self.user_service.get_by_username(username)

        if user is None:
            raise Exception()

        data = {
            "username": user.username,
            "role": user.role
        }

