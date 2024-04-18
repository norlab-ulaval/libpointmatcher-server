from os import environ as env

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import db.mongo as mongo
from adapter.libpointmatcher_adapter import LibpointmatcherAdapter
from db.evaluation_mongo import EvaluationMongo
from db.leaderboard_mongo import LeaderboardMongo
from db.users_mongo import UsersMongo
from evaluation.evaluation_controller import EvaluationController
from user.user_controller import UserController
from leaderboard.leaderboard_controller import LeaderboardController
from routers import example, auth, configs, leaderboard, evaluation
from routers.util import authorization

mongo_database = mongo.get_database(env)

user_mongo = UsersMongo(mongo_database)
evaluation_mongo = EvaluationMongo(mongo_database)
leaderboard_mongo = LeaderboardMongo(mongo_database)

libpointmatcher_adapter = LibpointmatcherAdapter()

user_controller = UserController(user_mongo)
leaderboard_controller = LeaderboardController(leaderboard_mongo)
evaluation_controller = EvaluationController(libpointmatcher_adapter, evaluation_mongo)

authorization.user_controller = user_controller
example.user_controller = user_controller
auth.user_controller = user_controller
leaderboard.leaderboard_controller = leaderboard_controller
configs.user_controller = user_controller
evaluation.evaluation_controller = evaluation_controller

# Build app
app = FastAPI()
app.include_router(example.router)
app.include_router(auth.router)
app.include_router(configs.router)
app.include_router(leaderboard.router)
app.include_router(evaluation.router)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def health():
    return {"Hello": "World"}
