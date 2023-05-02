from fastapi import Request, Response, FastAPI

from db import Mongo
from middleware import auth_middleware
from lib import respond


def get_current_user(app: FastAPI, mongo: Mongo):

    @app.get("/user")
    async def route_get_current_user(req: Request, res: Response):

        # getting the current user
        user, err = auth_middleware(req, mongo)
        if err != None:
            return respond(res, 'unauthorized', 401)

        # json response
        return respond(res, 'current user', data={
            '_id': str(user['_id']),
            'email': user['email'],
        })
