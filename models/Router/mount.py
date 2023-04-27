from models import HttpDriver
from models import MongoDriver
from .user_routes import *


def mount(self, http_driver: HttpDriver, mongo_driver: MongoDriver):
    create_user(http_driver=http_driver, mongo_driver=mongo_driver)
    delete_user(http_driver=http_driver, mongo_driver=mongo_driver)
    get_current_user(http_driver=http_driver, mongo_driver=mongo_driver)
    login_user(http_driver=http_driver, mongo_driver=mongo_driver)
    logout_user(http_driver=http_driver, mongo_driver=mongo_driver)
