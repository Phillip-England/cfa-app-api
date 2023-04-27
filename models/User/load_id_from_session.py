from models.HttpError import HttpError


def load_id_from_session(self, session_token, session_collection):
    if session_token == None:
        raise HttpError(401, 'unauthorized')
    result = session_collection.find_one({
        "token": session_token
    })
    if result == None:
        raise HttpError(401, 'unauthorized')
    self.id = str(result['user'])
