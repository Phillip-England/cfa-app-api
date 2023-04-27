from pydantic import BaseModel
from fastapi import Request, Response

from models import HttpDriver
from models import MongoDriver
from models import Store


def get_stores(http_driver: HttpDriver, mongo_driver: MongoDriver):

    @http_driver.app.get("/store")
    async def route_get_stores(request: Request, response: Response):
        try:
            user = http_driver.ConsumeEndpoint(request, response).Auth()
            stores = Store().FindAll(user.id, http_driver.store_collection)
            return http_driver.Success(200, 'got all stores', data=stores)
        except Exception as error:
            return http_driver.Fail(error)
