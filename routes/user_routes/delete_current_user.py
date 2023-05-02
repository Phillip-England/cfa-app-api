from fastapi import Request, Response, FastAPI
import pymongo

from db import Mongo
from db import delete_all
from db import delete_one
from middleware import auth_middleware


def delete_current_user(app: FastAPI, mongo: Mongo):

    @app.delete("/user")
    async def route_delete_current_user(request: Request, response: Response):

        # getting the logged in user
        user, err = auth_middleware(request, mongo)
        if err != None:
            response.status_code = 400
            return {'msg': 'unauthorized'}

        # dropping the user
        result = delete_one(mongo.users, {'_id': user['_id']})

        # dropping all user resources
        result = delete_all(mongo.sessions, {'user': user['_id']})
        result = delete_all(mongo.stores, {'user': user['_id']})

        # resetting session cookies
        response.set_cookie(
            key='session_token',
            value=''
        )

        # json response
        return {'msg': 'user deleted'}
