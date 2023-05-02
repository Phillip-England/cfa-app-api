import re

from bson import ObjectId


def v_max(value: str, max: int):
    if len(value) > max:
        return Exception('value length too long!')
    return None


def v_min(value: str, min: int):
    if len(value) < min:
        return Exception('value length too short')
    return None


def str_to_int(value: str):
    try:
        int(value)
        return None
    except:
        return Exception('string cannot be converted to int')


def str_to_objectid(value: str):
    try:
        ObjectId(value)
    except:
        return Exception('string cannot be converted to object id')


def v_email(email: str):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email) == None:
        return Exception('email is invalid')
    return None
