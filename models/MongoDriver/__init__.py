import pymongo
import os


class MongoDriver:
    def __init__(self, client: pymongo.MongoClient):
        self.client = client
        self.user_collection = client[os.getenv("DB_NAME")]['users']
        self.session_collection = client[os.getenv("DB_NAME")]['sessions']
        self.store_collection = client[os.getenv("DB_NAME")]['stores']
