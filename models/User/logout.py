from bson.objectid import ObjectId


def logout(self, response, session_collection):
    response.set_cookie(key="token", value="")
    result = session_collection.delete_one({"user": ObjectId(self.id)})
