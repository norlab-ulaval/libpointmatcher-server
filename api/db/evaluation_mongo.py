import asyncio
import os

from motor.core import AgnosticDatabase, AgnosticCollection

from db import mongo
from evaluation.evaluation import Evaluation
from evaluation.evaluation_repo import EvaluationRepo
from leaderboard.leaderboard_entry import LeaderboardEntry
from leaderboard.leaderboard_repo import LeaderboardRepo


def _to_json(evaluation: Evaluation):
    return {
        'run_id': evaluation.run_id,
        'user_email': evaluation.user_email,
        'type': evaluation.type,
        'result': evaluation.result,
        'date': evaluation.date,
        'anonymous': evaluation.anonymous
    }


def _from_json(json):
    return Evaluation(json['run_id'], json['user_email'], json['type'],
                      json['result'], json['date'], json['anonymous'])


class EvaluationMongo(EvaluationRepo, LeaderboardRepo):
    def __init__(self, mongo_database: AgnosticDatabase):
        self.collection: AgnosticCollection = mongo_database['evaluations']

    async def fetch_history_from_email(self, email: str) -> list[Evaluation]:
        evaluations = []

        cursor = (self.collection
                  .find({'user_email': email})
                  .sort([("date", -1)]))

        for doc in await cursor.to_list(length=None):
            evaluations.append(_from_json(doc))

        return evaluations

    async def save(self, evaluation: Evaluation):
        await self.collection.insert_one(_to_json(evaluation))

    async def find_all(self) -> list[LeaderboardEntry]:
        # TODO
        pass

    async def find_by_type(self, type: str) -> list[LeaderboardEntry]:
        # TODO
        pass

    async def get_all_types(self) -> list[str]:
        return await self.collection.find({}, {'type': 1}).distinct('type')

    async def get_size(self) -> int:
        return await self.collection.count_documents({})
