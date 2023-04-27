from models.HttpError import HttpError


def is_unique(self, user_collection):
    user_exists = user_collection.find_one(
        {"email": self.email})
    if user_exists != None:
        raise HttpError(400, "user already exists")
