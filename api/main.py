import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import db.mongo as mongo
from db.users_mongo import UsersMongo
from user.user_controller import UserController
from leaderboard.leaderboard_controller import LeaderboardController
from routers import example, auth, configs, leaderboard
from routers.util import authorization


env = os.environ

mongo_database = mongo.get_database(env)

user_repo = UsersMongo(mongo_database)
user_controller = UserController(user_repo)
leaderboard_controller = LeaderboardController()

authorization.user_controller = user_controller
example.user_controller = user_controller
auth.user_controller = user_controller
leaderboard.leaderboard_controller = leaderboard_controller
configs.user_controller = user_controller

# Build app
app = FastAPI()
app.include_router(example.router)
app.include_router(auth.router)
app.include_router(configs.router)
app.include_router(leaderboard.router)

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
