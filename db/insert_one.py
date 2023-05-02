from pymongo.collection import Collection


def insert_one(collection: Collection, filter: dict):
    result = collection.insert_one(filter)
    return result
