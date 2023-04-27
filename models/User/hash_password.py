import bcrypt


def hash_password(self):
    salt = bcrypt.gensalt()
    password_bytes = self.password.encode()
    self.hashed_password = bcrypt.hashpw(password_bytes, salt)
