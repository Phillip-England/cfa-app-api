import datetime

from fastapi import Request, Response, FastAPI
import pymongo

from db import load_collection
from lib import error_response
from lib import success_response
from middleware import auth_middleware


def logout_user(app: FastAPI, client: pymongo.MongoClient):

    user_collection = load_collection(client, 'users')
    session_collection = load_collection(client, 'sessions')

    @app.get("/user/logout")
    async def route_logout_user(request: Request, response: Response):
        try:
            user = auth_middleware(
                request, session_collection, user_collection)
            delete_count = session_collection.delete_many({
                'user': user['_id']
            })
            response.set_cookie(
                key='session_token',
                value=''
            )
            return success_response(response, 200, 'user logged out')
        except Exception as error:
            return error_response(response, error)
