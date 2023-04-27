from pydantic import BaseModel
from fastapi import Request, Response

from models import HttpDriver
from models import MongoDriver
from models import Store


def create_store(http_driver: HttpDriver, mongo_driver: MongoDriver):

    class CreateStoreRequest(BaseModel):
        name: str
        number: str

    @http_driver.app.post("/store")
    async def route_create_store(body: CreateStoreRequest, request: Request, response: Response):
        try:
            user = http_driver.ConsumeEndpoint(request, response).Auth()
            store_response = Store(body.name, body.number).Create(
                user.id, http_driver.store_collection)
            return http_driver.Success(201, 'store created', data=store_response)
        except Exception as error:
            return http_driver.Fail(error)
