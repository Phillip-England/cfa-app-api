from fastapi import Request, Response, FastAPI
from pydantic import BaseModel

from db import Mongo
from middleware import auth_middleware


def update_store(app: FastAPI, mongo: Mongo):

    class RequestBody(BaseModel):
        name: str
        number: str

    @app.put("/store/{id}")
    async def route_update_store(body: RequestBody, req: Request, res: Response, id: str):

        # getting the current user
        user = auth_middleware(req, mongo)
        name = body.name
        number = body.number
