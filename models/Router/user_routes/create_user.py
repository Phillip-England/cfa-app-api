from fastapi import Request, Response
from pydantic import BaseModel

from models import HttpDriver
from models import MongoDriver
from models import User


def create_user(http_driver: HttpDriver, mongo_driver: MongoDriver):
    class CreateUserRequest(BaseModel):
        email: str
        password: str

    @http_driver.app.post("/user")
    async def route_create_user(body: CreateUserRequest, request: Request, response: Response):
        try:
            http_driver.ConsumeEndpoint(request, response)
            user = User(email=body.email, password=body.password).Create(
                http_driver.user_collection)
            return http_driver.Success(201, 'user created', data=user.SuccessResponse())
        except Exception as error:
            return http_driver.Fail(error)
