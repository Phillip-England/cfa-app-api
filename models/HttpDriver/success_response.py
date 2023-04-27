from fastapi import Response


def success_response(self, response: Response, status_code: int, message: str, data: dict = {}):
    response.status_code = status_code
    return {
        'msg': message,
        'data': data
    }
