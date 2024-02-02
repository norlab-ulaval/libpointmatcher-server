import motor.motor_asyncio

import os

from motor.core import AgnosticCollection

DATABASE = os.environ['MONGO_DATABASE']
USERNAME = os.environ['MONGO_USERNAME']
PASSWORD = os.environ['MONGO_PASSWORD']
CONNECTION_STRING = "mongodb://${USERNAME}:${PASSWORD}@mongo:27017/".format(
    USERNAME=USERNAME, PASSWORD=PASSWORD
)

client = motor.motor_asyncio.AsyncIOMotorClient(CONNECTION_STRING)
db = client[DATABASE]


def get_collection(collection_name: str) -> AgnosticCollection:
    return db[collection_name]


