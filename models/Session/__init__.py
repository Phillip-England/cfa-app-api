from .create import create


class Session:
    def __init__(self, user_id):
        self.user_id = user_id

    create = create