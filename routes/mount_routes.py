from fastapi import FastAPI
from pymongo import MongoClient

from .user_routes import *


def mount_routes(app: FastAPI, client: MongoClient):
    create_user(app, client)
    login_user(app, client)
    get_current_user(app, client)
    logout_user(app, client)
    delete_current_user(app, client)
