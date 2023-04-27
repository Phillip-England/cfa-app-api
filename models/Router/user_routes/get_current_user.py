from fastapi import Request, Response

from models import HttpDriver
from models import MongoDriver


def get_current_user(http_driver: HttpDriver, mongo_driver: MongoDriver):

    @http_driver.app.get("/user")
    async def route_get_current_user(request: Request, response: Response):
        try:
            user = http_driver.ConsumeEndpoint(request, response).Auth()
            return http_driver.Success(200, 'user loaded', data=user.SuccessResponse())
        except Exception as error:
            return http_driver.Fail(error)
