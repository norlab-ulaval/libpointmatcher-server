import os

from fastapi import FastAPI

from api.db import mongo
from api.db.users_mongo import UsersMongo
from api.user.user_controller import UserController
from routers import example


env = os.environ

mongo_database = mongo.get_database(env)

user_repo = UsersMongo(mongo_database)
user_controller = UserController(user_repo)

example.user_controller = user_controller

# Build app
app = FastAPI()
app.include_router(example.router)


# TODO remove later
@app.get("/")
def hello_world():
    return {"Hello": "World"}
