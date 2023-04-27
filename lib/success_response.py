from fastapi import Response


def success_response(response: Response, status_code: int, message: str, data: dict = {}):
    response.status_code = status_code
    if data:
        return {
            'msg': message,
            'data': data
        }
    return {
        'msg': message
    }
