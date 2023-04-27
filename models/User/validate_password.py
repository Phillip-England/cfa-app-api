from models.HttpError import HttpError


def validate_password(self):
    if self.password == None or len(self.password) == 0:
        raise HttpError(400, 'password is required')
    if len(self.password) < 8:
        raise HttpError(400, 'password must contain 8 or more characters')
    if len(self.password) > 64:
        raise HttpError(
            400, 'password must contain no more than 64 characters')
