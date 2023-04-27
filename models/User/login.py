from models import Session


def login(self, response, user_collection, session_collection):
    self.Format()
    self.PullByEmail(user_collection)
    self.ConfirmPassword()
    self.session_token = Session(
        user_id=self.id).Create(response, session_collection)
    return self
