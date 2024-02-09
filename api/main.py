import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import db.mongo as mongo
from db.users_mongo import UsersMongo
from user.user_controller import UserController
from routers import example, auth, configs


env = os.environ

mongo_database = mongo.get_database(env)

user_repo = UsersMongo(mongo_database)
user_controller = UserController(user_repo)

example.user_controller = user_controller

# Build app
app = FastAPI()
app.include_router(example.router)
app.include_router(auth.router)
app.include_router(configs.router)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# TODO remove later
@app.get("/")
def hello_world():
    return {"Hello": "World"}
