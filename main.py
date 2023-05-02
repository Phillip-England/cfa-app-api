import os

from fastapi import FastAPI
from dotenv import load_dotenv
import pymongo

from middleware import cors_middleware
from routes import mount_routes
from db import Mongo


load_dotenv()
app = FastAPI()
app = cors_middleware(app=app)
mongo = Mongo(client=pymongo.MongoClient(os.getenv("MONGO_URI")))
mount_routes(app=app, mongo=mongo)
