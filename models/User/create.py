def create(self, user_collection):
    self.format()
    self.run_validation()
    self.is_unique(user_collection)
    self.hash_password()
    self.insert(user_collection)
    return self
