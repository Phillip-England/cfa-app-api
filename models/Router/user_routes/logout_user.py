from fastapi import Request, Response

from models import HttpDriver
from models import MongoDriver


def logout_user(http_driver: HttpDriver, mongo_driver: MongoDriver):
    @ http_driver.app.get("/user/logout")
    async def route_logout_user(request: Request, response: Response):
        try:
            user = http_driver.ConsumeEndpoint(request, response).Auth()
            user.Logout(http_driver.response, http_driver.session_collection)
            return http_driver.Success(200, 'user logged out')
        except Exception as error:
            return http_driver.Fail(error)
