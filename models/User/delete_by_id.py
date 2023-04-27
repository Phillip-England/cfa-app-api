from bson.objectid import ObjectId


from models.HttpError import HttpError


def delete_by_id(self, id, user_collection, session_collection):
    if len(id) != 24:
        raise HttpError(404, 'not found')
    if id != self.id:
        raise HttpError(403, 'forbidden request')
    doc_id = ObjectId(id)
    result = user_collection.delete_one({"_id": doc_id})
    if result.deleted_count == 0:
        raise HttpError(404, 'failed to delete user')
    result = session_collection.delete_one({'user': ObjectId(self.id)})
