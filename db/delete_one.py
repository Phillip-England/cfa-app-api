from pymongo.collection import Collection


def delete_one(collection: Collection, filter: dict):
    result = collection.delete_one(filter)
    return result
