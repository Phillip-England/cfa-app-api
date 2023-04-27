import bcrypt


def hash_password(password: str):
    salt = bcrypt.gensalt()
    password_bytes = password.encode()
    return bcrypt.hashpw(password_bytes, salt).decode('utf-8')
