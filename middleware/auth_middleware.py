import datetime

from bson.objectid import ObjectId
from fastapi import Request
from pymongo import collection


def auth_middleware(request: Request, session_collection: collection, user_collection: collection):
    if 'session_token' not in request.cookies.keys():
        raise Exception(401, 'unauthorized')
    session_token = request.cookies['session_token']
    try:
        session_id = ObjectId(session_token)
    except Exception:
        raise Exception(401, 'unauthorized')
    session = session_collection.find_one({
        '_id': ObjectId(session_token)
    })
    if session == None:
        raise Exception(401, 'session does not exist')
    if datetime.datetime.now() > datetime.datetime.fromisoformat(session['expires']):
        raise Exception(401, 'session expired')
    user = user_collection.find_one({
        '_id': session['user']
    })
    if user == None:
        raise Exception(401, 'no user associated with session')
    return user
