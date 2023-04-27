from models.HttpError import HttpError


def pull_by_email(self, user_collection):
    user_exists = user_collection.find_one(
        {'email': self.email})
    if user_exists == None:
        raise HttpError(400, "invalid credentials")
    self.db_password = user_exists['password']
    self.id = user_exists['_id']
