import os

from fastapi import FastAPI

from api import dependencies
from api.db import mongo
from routers import example


env = os.environ


# Load dependencies
dependencies.mongo_database = mongo.get_database(env)


# Build app
app = FastAPI()
app.include_router(example.router)


# TODO remove later
@app.get("/")
def hello_world():
    return {"Hello": "World"}
