from pymongo.collection import Collection


def find_one(collection: Collection, filter: dict):
    result = collection.find_one(filter)
    return result
