
def auth(self, session_token, user_collection, session_collection):
    self.session_token = session_token
    self.LoadIDFromSession(session_token, session_collection)
    self.PullByID(user_collection)
    return self
