from fastapi import FastAPI

from .cors_middleware import cors_middleware
from .auth_middleware import auth_middleware
from .success_response import success_response
from .error_response import error_response


class HttpDriver:
    def __init__(self, app: FastAPI):
        self.app = app

    auth_middleware = auth_middleware
    cors_middleware = cors_middleware
    success_response = success_response
    error_response = error_response
