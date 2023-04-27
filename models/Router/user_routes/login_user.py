from fastapi import Request, Response
from pydantic import BaseModel

from models import HttpDriver
from models import MongoDriver
from models import User


def login_user(http_driver: HttpDriver, mongo_driver: MongoDriver):

    class LoginUserRequest(BaseModel):
        email: str
        password: str

    @http_driver.app.post("/user/login")
    async def route_login_user(body: LoginUserRequest, request: Request, response: Response):
        try:
            http_driver.ConsumeEndpoint(request, response)
            user = User(email=body.email, password=body.password).Login(http_driver.response,
                                                                        http_driver.user_collection, http_driver.session_collection)
            return http_driver.Success(200, 'user logged in')
        except Exception as error:
            return http_driver.Fail(error)
