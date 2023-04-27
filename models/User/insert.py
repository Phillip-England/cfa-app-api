def insert(self, user_collection):
    result = user_collection.insert_one({
        "email": self.email,
        'password': self.hashed_password
    })
    self.id = str(result.inserted_id)
