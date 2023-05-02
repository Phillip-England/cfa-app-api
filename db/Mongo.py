import os

from pymongo import MongoClient


class Mongo:
    def __init__(self, client: MongoClient):
        self.client = client
        self.users = client[os.getenv("DB_NAME")][os.getenv("DB_USERS")]
        self.sessions = client[os.getenv("DB_NAME")][os.getenv("DB_SESSIONS")]
        self.stores = client[os.getenv("DB_NAME")][os.getenv("DB_STORES")]

    def drop_all(self):
        self.users.delete_many({})
        self.stores.delete_many({})
        self.sessions.delete_many({})
