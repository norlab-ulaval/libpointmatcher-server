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
        entries = []

        cursor = self.collection.aggregate([
            {'$sort': {'result': 1}},
            {'$group': {
                '_id': {'user_email': '$user_email', 'type': '$type'},
                'result': {'$first': '$result'},
                'date': {'$first': '$date'},
                'anonymous': {'$first': '$anonymous'}
            }}
        ])

        for doc in await cursor.to_list(length=None):
            email = '' if doc['anonymous'] else doc['_id']['user_email']
            entries.append(LeaderboardEntry(username=email, score=doc['result'], score_type=doc['_id']['type'], version='demo', date=doc['date']))

        return entries

    async def find_by_type(self, type: str) -> list[LeaderboardEntry]:
        entries = []

        cursor = self.collection.aggregate([
            {'$match': {'type': type}},
            {'$sort': {'result': 1}},
            {'$group': {
                '_id': '$user_email',
                'result': {'$first': '$result'},
                'date': {'$first': '$date'},
                'anonymous': {'$first': '$anonymous'}
            }}
        ])

        for doc in await cursor.to_list(length=None):
            email = '' if doc['anonymous'] else doc['_id']
            entries.append(LeaderboardEntry(username=email, score=doc['result'], score_type=type, version='demo', date=doc['date']))

        return entries
      
    async def get_all_types(self) -> list[str]:
        return await self.collection.find({}, {'type': 1}).distinct('type')
