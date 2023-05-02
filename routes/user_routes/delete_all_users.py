from fastapi import Request, Response, FastAPI

from db import Mongo
from lib import respond


def delete_all_users(app: FastAPI, mongo: Mongo):

    @app.delete("/user/delete/all")
    async def route_delete_all_users(req: Request, res: Response):
        try:
            session_delete_count = mongo.sessions.delete_many({})
            store_delete_count = mongo.stores.delete_many({})
            user_delete_count = mongo.users.delete_many({})
            return respond(res, 200, 'all users deleted')
        except Exception as error:
            print(error)
            return respond(res, error)
