from fastapi import Response


def error_response(response: Response, error: Exception):
    if len(error.args) >= 2:
        status_code = error.args[0]
        message = error.args[1]
        if status_code and message:
            response.status_code = status_code
            return {
                'msg': message
            }
    response.status_code = 500
    return {
        'msg': 'internal server error'
    }
