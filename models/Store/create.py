import pymongo


def create(self, user_id: str, store_collection):
    self.user = user_id
    self.validate_name()
    self.validate_number()
    self.is_unique(store_collection)
    self.insert(user_id, store_collection)
    return self.success_response()
