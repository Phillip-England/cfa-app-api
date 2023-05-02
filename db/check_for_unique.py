from pymongo.collection import Collection


def check_for_unique(collection: Collection, filter: dict):
    document_exists = collection.find_one(filter)
    if document_exists != None:
        return Exception('document already exists')
    return None
