from pymongo import MongoClient
import os


def load_collection(client: MongoClient, collection_name: str):
    return client[os.getenv("DB_NAME")][collection_name]
