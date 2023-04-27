from fastapi import Response
from models import HttpError


def error_response(self, response: Response, err: any):
    if isinstance(err, HttpError):
        response.status_code = err.status_code
        return {
            "msg": err.message
        }
    print(err)
    response.status_code = 500
    return {
        "msg": "internal server error"
    }
