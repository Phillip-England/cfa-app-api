import datetime

from fastapi import Request, Response, FastAPI
from pydantic import BaseModel
from bson import ObjectId

from db import Mongo
from middleware import auth_middleware
from lib import v_max, v_min, str_to_int, respond


def create_store(app: FastAPI, mongo: Mongo):

    class RequestBody(BaseModel):
        name: str
        number: str

    @app.post("/store")
    async def route_create_store(body: RequestBody, req: Request, res: Response):

        # getting the logged in user
        user, err = auth_middleware(req, mongo)
        if err != None:
            return respond(res, 'unauthorized', 401)

        # unpacking values
        name = body.name
        number = body.number

        # formatting name
        name = name.lower().strip()

        # validating name
        if v_min(name, 3) != None:
            return respond(res, 'name too short', 400)
        if v_max(name, 64) != None:
            return respond(res, 'name too long', 400)

        # validating number
        if str_to_int(number) != None:
            return respond(res, 'must provide a number', 400)
        if v_min(number, 1) != None:
            return respond(res, 'number too short', 400)
        if v_max(number, 12) != None:
            return respond(res, 'number too long', 400)

        # checking is the user already has a store with this name
        name_exists = mongo.stores.find_one(
            {'user': user["_id"], 'name': name})
        if name_exists != None:
            return respond(res, 'name already exists', 400)

        # checking if the user already has a store with this number
        number_exists = mongo.stores.find_one(
            {'user': user["_id"], 'number': number})
        if number_exists != None:
            return respond(res, 'number already exists', 400)

        # inserting the store into db
        result = mongo.stores.insert_one({
            'user': ObjectId(user['_id']),
            'created_at': datetime.datetime.now().isoformat(),
            'updated_at': datetime.datetime.now().isoformat(),
            'name': name,
            'number': number
        })

        # json response
        return respond(res, 'store created', data={
            '_id': str(result.inserted_id),
            'name': name,
            'number': number
        })
