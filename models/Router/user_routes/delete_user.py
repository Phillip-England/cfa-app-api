
from fastapi import Request, Response

from models import HttpDriver
from models import MongoDriver


def delete_user(http_driver: HttpDriver, mongo_driver: MongoDriver):

    @http_driver.app.delete("/user/{id}")
    async def route_delete_user(id: str, request: Request, response: Response):
        try:
            user = http_driver.ConsumeEndpoint(request, response).Auth()
            user.DeleteByID(id, http_driver.user_collection,
                            http_driver.session_collection)
            return http_driver.Success(200, 'user deleted')
        except Exception as error:
            return http_driver.Fail(error)
