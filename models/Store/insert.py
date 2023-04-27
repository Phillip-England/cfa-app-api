from bson.objectid import ObjectId


def insert(self, user_id: str, store_collection):
    doc_id = ObjectId(user_id)
    result = store_collection.insert_one({
        'user': doc_id,
        'name': self.name,
        'number': self.number
    })
    self.id = str(result.inserted_id)
