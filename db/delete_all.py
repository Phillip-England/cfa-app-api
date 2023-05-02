from pymongo.collection import Collection


def delete_all(collection: Collection, filter: dict):
    result = collection.delete_many(filter)
    return result
