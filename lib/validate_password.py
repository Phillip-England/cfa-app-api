def validate_password(password: str):
    if password == None or len(password) == 0:
        raise Exception(400, 'password is required')
    if len(password) < 8:
        raise Exception(400, 'password must contain 8 or more characters')
    if len(password) > 64:
        raise Exception(
            400, 'password must contain no more than 64 characters')
    return password
