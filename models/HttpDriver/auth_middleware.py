from models.User import User


def auth_middleware(self):
    user = User().Auth(self.request.cookies.get('token'),
                       self.user_collection, self.session_collection)
    return user
