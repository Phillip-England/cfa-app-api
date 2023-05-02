import datetime

from bson.objectid import ObjectId
from fastapi import Request

from db import Mongo


def auth_middleware(request: Request, mongo: Mongo):
    session_token = request.cookies['session_token']
    if session_token == '':
        return None, Exception('session does not exist')
    session = mongo.sessions.find_one({'_id': ObjectId(session_token)})
    if session == None:
        return None, Exception('no session associated with token')
    if datetime.datetime.now() > datetime.datetime.fromisoformat(session['expires_at']):
        return None, Exception('session expired')
    user = mongo.users.find_one({
        '_id': ObjectId(session['user'])
    })
    if user == None:
        return None, Exception('no user associated with session')
    return user, None
