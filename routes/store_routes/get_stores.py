import json

from fastapi import Request, Response, FastAPI

from db import Mongo
from middleware import auth_middleware
from lib import respond


def get_stores(app: FastAPI, mongo: Mongo):

    @app.get("/store")
    async def route_get_stores(req: Request, res: Response, min: int = None, max: int = None):

        # getting the current user
        user, err = auth_middleware(req, mongo)
        if err != None:
            return respond(res, 'unauthorized', 401)

        # getting all user stores
        stores = mongo.stores.find({
            'user': user['_id']
        })

        # building a list of stores to be returned
        stores_list = []
        if stores != None:
            for store in stores:
                stores_list.append({
                    '_id': str(store['_id']),
                    'created_at': store['created_at'],
                    'name': store['name'],
                    'number': store['number']
                })

        # checking is we have query params
        if min != None and max != None:

            # if we do, return a slice of stores back to client
            stores_slice = stores_list[min:max]
            return respond(res, 'here are your stores', data=stores_slice)

        # send all stores if not query params are provided
        return respond(res, 'here are your stores', data=stores_list)
