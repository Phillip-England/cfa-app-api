import os

from fastapi import FastAPI
from dotenv import load_dotenv
import pymongo

from middleware import cors_middleware
from routes import mount_routes


load_dotenv()
app = FastAPI()
app = cors_middleware(app)
client = pymongo.MongoClient(os.getenv("MONGO_URI"))
mount_routes(app, client)
