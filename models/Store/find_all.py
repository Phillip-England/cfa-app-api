from bson.objectid import ObjectId
from models import Store


def find_all(self, user_id: str, store_collection):
    self.user = user_id
    documents = store_collection.find({
        'user': ObjectId(self.user)
    })
    stores = []
    for doc in documents:
        store = Store(name=doc['name'], number=doc['number'], user=str(
            doc['user']), id=str(doc['_id']))
        stores.append(store)
    return stores
