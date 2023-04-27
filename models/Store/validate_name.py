from models.HttpError import HttpError


def validate_name(self):
    if len(self.name) < 3:
        raise HttpError(400, 'name must contain 3 or more characters')
    if len(self.name) > 64:
        raise HttpError(400, 'name must contain less than 64 characters')
