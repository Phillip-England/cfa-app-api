import bcrypt


def confirm_password(self):
    passwords_match = bcrypt.checkpw(
        self.password.encode("utf-8"), self.db_password)
    if passwords_match == False:
        raise HttpError(400, "invalid credentials")
