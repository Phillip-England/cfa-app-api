from fastapi import Request, Response, FastAPI
from bson import ObjectId

from db import Mongo
from middleware import auth_middleware

from lib import respond, str_to_objectid


def delete_store_by_id(app: FastAPI, mongo: Mongo):

    @app.delete("/store/{id}")
    async def route_delete_store_by_id(req: Request, res: Response, id: str):

        # getting the current user
        user, err = auth_middleware(req, mongo)
        if err != None:
            return respond(res, 'unauthorized', 401)

        # checking if the passed in id is a valid mongo id
        if str_to_objectid(id) != None:
            return respond(res, 'invalid id', 400)

        # converting id to an object id
        id = ObjectId(id)

        # checking if a store with the id exists
        store_exists = mongo.stores.find_one({
            '_id': id
        })

        # if the store doesn't exist, exit
        if store_exists == None:
            return respond(res, 'invalid id', 400)

        # checking if the store belongs to the current user
        if store_exists['user'] != user['_id']:
            return respond(res, 'forbidden', 403)

        # deleting the store
        result = mongo.stores.delete_one({'_id': id})

        # json response
        return respond(res, 'success', data={
            'stores_deleted': result.deleted_count
        })
