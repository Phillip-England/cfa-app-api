from fastapi import Response


def respond(response: Response, message: str, status_code: int = 200, data: dict = {}):
    response.status_code = status_code
    if data != {}:
        return {
            'msg': message,
            'data': data
        }
    return {'msg': message}
