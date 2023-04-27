import datetime

from fastapi import Request, Response, FastAPI
from pydantic import BaseModel
import pymongo

from db import load_collection
from lib import error_response
from lib import success_response
from lib import check_password


def login_user(app: FastAPI, client: pymongo.MongoClient):

    user_collection = load_collection(client, 'users')
    session_collection = load_collection(client, 'sessions')

    class RequestBody(BaseModel):
        email: str
        password: str

    @app.post("/user/login")
    async def route_login_user(body: RequestBody, request: Request, response: Response):
        try:
            user = user_collection.find_one({
                'email': body.email
            })
            if user == None:
                raise Exception(400, 'invalid credentials')
            check_password(
                body.password, user['password'], 'invalid credentials')
            delete_count = session_collection.delete_many({
                'user': user['_id']
            })
            expiration_time = datetime.datetime.now() + datetime.timedelta(days=1)
            iso_expiration_time = expiration_time.isoformat()
            result = session_collection.insert_one({
                'user': user['_id'],
                'expires': iso_expiration_time
            })
            session_id = result.inserted_id
            response.set_cookie(
                key='session_token',
                value=session_id,
                expires=86400,  # 24 hours in seconds
                httponly=True
            )
            return success_response(response, 200, 'success')
        except Exception as error:
            return error_response(response, error)
