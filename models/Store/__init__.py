from .create import create
from .find_all import find_all
from .insert import insert
from .is_unique import is_unique
from .success_response import success_response
from .validate_name import validate_name
from .validate_number import validate_number


class Store:
    def __init__(self, name=None, number=None, user=None, id=None):
        self.name = name
        self.number = number
        self.user = user
        self.id = id
