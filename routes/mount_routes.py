from fastapi import FastAPI

from db import Mongo
from .user_routes import *
from .store_routes import *


def mount_routes(app: FastAPI, mongo: Mongo):
    create_user(app=app, mongo=mongo)
    login_user(app=app, mongo=mongo)
    get_current_user(app=app, mongo=mongo)
    logout_user(app=app, mongo=mongo)
    delete_current_user(app=app, mongo=mongo)
    create_store(app=app, mongo=mongo)
    get_stores(app=app, mongo=mongo)
    delete_store_by_id(app=app, mongo=mongo)
    delete_all_users(app=app, mongo=mongo)
    update_store(app=app, mongo=mongo)
