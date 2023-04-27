import re


def validate_email(email: str):
    if email == None or len(email) == 0:
        raise Exception(400, 'please provide a valid email')
    if len(email) > 64:
        raise Exception(400, 'email to long')
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email) == None:
        raise Exception(400, 'please enter a valid email')
    return email
