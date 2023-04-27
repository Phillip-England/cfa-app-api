from bson.objectid import ObjectId

from models.HttpError import HttpError


def is_unique(self, store_collection):
    store_exists = store_collection.find_one({
        'user': ObjectId(self.user),
        'name': self.name
    })
    if store_exists != None:
        raise HttpError(400, 'store already exists')
