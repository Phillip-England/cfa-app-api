from fastapi import Request, Response, FastAPI
from pydantic import BaseModel
import pymongo

from db import load_collection
from lib import validate_email
from lib import format_email
from lib import validate_password
from lib import error_response
from lib import success_response
from lib import hash_password


def create_user(app: FastAPI, client: pymongo.MongoClient):

    user_collection = load_collection(client, "users")

    class RequestBody(BaseModel):
        email: str
        password: str

    @app.post("/user")
    async def route_create_user(body: RequestBody, request: Request, response: Response):
        try:
            valid_email = validate_email(format_email(body.email))
            valid_password = hash_password(validate_password(body.password))
            user_exists = user_collection.find_one({
                'email': valid_email
            })
            if user_exists != None:
                raise Exception(400, 'user already exists')
            result = user_collection.insert_one({
                'email': valid_email,
                'password': valid_password
            })
            user_id = result.inserted_id
            return success_response(response, 201, 'user created', {
                '_id': str(user_id),
                'email': valid_email
            })
        except Exception as error:
            return error_response(response, error)
