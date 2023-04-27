
from bson.objectid import ObjectId

from models.HttpError import HttpError


def pull_by_id(self, user_collection):
    user = user_collection.find_one({
        '_id': ObjectId(self.id)
    })
    if user == None:
        raise HttpError(401, "unauthorized")
    self.email = user['email']
    self.password = user['password']
