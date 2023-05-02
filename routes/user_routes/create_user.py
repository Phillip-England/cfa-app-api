from fastapi import Request, Response, FastAPI
from pydantic import BaseModel

from lib import v_email, hash_string, respond, v_max, v_min
from db import check_for_unique, insert_one, Mongo


def create_user(app: FastAPI, mongo: Mongo):

    # purpose - to get the incoming request body
    class RequestBody(BaseModel):
        email: str
        password: str

    @app.post("/user")
    async def route_create_user(body: RequestBody, req: Request, res: Response):

        # formatting user data and extracting values
        email = body.email.lower().strip()
        password = body.password

        # validating password
        if v_min(password, 5) != None:
            return respond(res, 'password too short', 400)
        if v_max(password, 64) != None:
            return respond(res, 'password too long', 400)

        # validing email
        if v_email(email) != None:
            return respond(res, 'invalid email', 400)

        # checking if the user is unique
        if check_for_unique(mongo.users, {'email': email}) != None:
            return respond(res, 'user already exists', 400)

        # hashing password
        password = hash_string(password)

        # storing the user in the db
        result = insert_one(mongo.users, {
            'email': email,
            'password': password
        })

        # json response
        return {
            '_id': str(result.inserted_id),
            'email': email
        }
