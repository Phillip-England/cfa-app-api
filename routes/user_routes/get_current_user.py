import datetime

from fastapi import Request, Response, FastAPI
import pymongo

from db import load_collection
from middleware import auth_middleware
from lib import error_response
from lib import success_response


def get_current_user(app: FastAPI, client: pymongo.MongoClient):

    user_collection = load_collection(client, 'users')
    session_collection = load_collection(client, 'sessions')

    @app.get("/user")
    async def route_get_current_user(request: Request, response: Response):
        try:
            user = auth_middleware(
                request, session_collection, user_collection)
            return success_response(response, 200, 'success', {
                '_id': str(user['_id']),
                'email': user['email'],
            })
        except Exception as error:
            return error_response(response, error)
