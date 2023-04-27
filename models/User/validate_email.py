import re
from models import HttpError


def validate_email(self):
    if self.email == None or len(self.email) == 0:
        raise HttpError(400, 'email is required')
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, self.email) == None:
        raise HttpError(400, 'please provide a valid email address')
