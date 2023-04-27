import bcrypt


def check_password(password: str, hashed_password: str, error_message: str):
    passwords_match = bcrypt.checkpw(password.encode(
        'utf-8'), hashed_password.encode('utf-8'))
    if passwords_match == False:
        raise Exception(400, error_message)
