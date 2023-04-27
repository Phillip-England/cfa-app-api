import secrets


def create(self, session_collection):
    deleted_sessions = session_collection.delete_one(
        {"user": self.user_id})
    session_token = secrets.token_hex(128)
    result = session_collection.insert_one({
        "user": self.user_id,
        "token": session_token
    })
    self.id = str(result.inserted_id)
    return session_token
