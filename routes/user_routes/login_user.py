import datetime

from fastapi import Request, Response, FastAPI
from pydantic import BaseModel
from bson import ObjectId

from db import Mongo, find_one, delete_all, insert_one
from lib import compare_hash, days_in_future, respond


def login_user(app: FastAPI, mongo: Mongo):

    class RequestBody(BaseModel):
        email: str
        password: str

    @app.post("/user/login")
    async def route_login_user(body: RequestBody, req: Request, res: Response):

        # unpacking request body
        email = body.email
        password = body.password

        # pulling provided user
        provided_user = find_one(mongo.users, {'email': email})
        if provided_user == None:
            return respond(res, 'invalid credentails', 400)

        # checking is password is correct
        if compare_hash(password, provided_user['password']) != None:
            return respond(res, 'invalid credentials', 400)

        # dropping all user sessions
        result = delete_all(
            mongo.sessions, {'user': ObjectId(provided_user['_id'])})

        # creating a new user session
        result = insert_one(mongo.sessions, {
            'user': ObjectId(provided_user['_id']),
            'created_at': days_in_future(0).isoformat(),
            'expires_at': days_in_future(1).isoformat()
        })

        # creating a http cookie with session
        res.set_cookie(key='session_token', value=str(
            result.inserted_id), expires=days_in_future(1).isoformat())

        # json response
        return respond(res, 'success')
