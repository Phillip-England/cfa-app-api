import datetime

from fastapi import Request, Response, FastAPI
import pymongo

from db import Mongo, delete_all
from middleware import auth_middleware
from lib import respond


def logout_user(app: FastAPI, mongo: Mongo):

    @app.get("/user/logout")
    async def route_logout_user(req: Request, res: Response):

        # getting logged in user
        user, err = auth_middleware(req, mongo)
        if err != None:
            respond(res, 'unauthorized', 400)

        # removing all sessions associated with user
        result = delete_all(mongo.sessions, {'user': user['_id']})

        # deleting session data from http cookie
        res.set_cookie(
            key='session_token',
            value=''
        )

        # json response
        return respond(res, 'user logged out')
