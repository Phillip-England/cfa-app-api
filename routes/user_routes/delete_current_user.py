from fastapi import Request, Response, FastAPI
import pymongo

from db import load_collection
from middleware import auth_middleware
from lib import error_response
from lib import success_response


def delete_current_user(app: FastAPI, client: pymongo.MongoClient):

    user_collection = load_collection(client, 'users')
    session_collection = load_collection(client, 'sessions')

    @app.delete("/user")
    async def route_delete_current_user(request: Request, response: Response):
        try:
            user = auth_middleware(
                request, session_collection, user_collection)
            session_delete_count = session_collection.delete_many({
                'user': user['_id']
            })
            user_delete_count = user_collection.delete_one(
                {'_id': user['_id']})
            response.set_cookie(
                key='session_token',
                value=''
            )
            return success_response(response, 200, 'user deleted')
        except Exception as error:
            print(error)
            return error_response(response, error)
