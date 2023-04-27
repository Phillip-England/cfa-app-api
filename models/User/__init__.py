from .auth import auth
from .confirm_password import confirm_password
from .create import create
from .delete_by_id import delete_by_id
from .format import format
from .hash_password import hash_password
from .is_unique import is_unique
from .load_id_from_session import load_id_from_session
from .login import login
from .logout import logout
from .pull_by_email import pull_by_email
from .pull_by_id import pull_by_id
from .run_validation import run_validation
from .success_response import success_response
from .validate_email import validate_email
from .validate_password import validate_password


class User:
    def __init__(self, email=None, password=None):
        self.email = email
        self.password = password
        self.db_password = None
        self.id = None
        self.session_token = None
