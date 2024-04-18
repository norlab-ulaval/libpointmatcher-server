from motor.core import AgnosticDatabase, AgnosticCollection

from evaluation.evaluation import Evaluation, Iteration
from evaluation.evaluation_repo import EvaluationRepo
from leaderboard.leaderboard_entry import LeaderboardEntry
from leaderboard.leaderboard_repo import LeaderboardRepo


def _to_json(evaluation: Evaluation):
    iterations = []

    for iteration in evaluation.iterations:
        iterations.append({
            'rotation_error': iteration.rotation_error,
            'translation_error': iteration.translation_error,
            'transformation': iteration.transformation
        })

    return {
        'run_id': evaluation.run_id,
        'user_email': evaluation.user_email,
        'type': evaluation.type,
        'evaluation_name': evaluation.evaluation_name,
        'file_name': evaluation.file_name,
        'iterations': iterations,
        'date': evaluation.date,
        'anonymous': evaluation.anonymous
    }


def _from_json(json):
    iterations = []

    for iteration_json in json['iterations']:
        iterations.append(Iteration(iteration_json['rotation_error'], iteration_json['translation_error'],
                                    iteration_json['transformation']))

    return Evaluation(json['run_id'], json['user_email'], json['type'], json['evaluation_name'],
                      json['file_name'], json['iterations'], json['date'], json['anonymous'])


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

    # TODO move to own repo
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

    # TODO move to own repo
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

    # TODO move to own repo
    async def find_by_type_and_limits(self, type: str, page: int, per_page: int) -> list[LeaderboardEntry]:
        entries = []
        skip_count = per_page * (page - 1)

        cursor = self.collection.aggregate([
            {'$match': {'type': type}},
            {'$sort': {'result': 1}},
            {'$group': {
                '_id': '$user_email',
                'result': {'$first': '$result'},
                'date': {'$first': '$date'},
                'anonymous': {'$first': '$anonymous'}
            }},
            {'$skip': skip_count},
            {'$limit': per_page}
        ])

        for doc in await cursor.to_list(length=None):
            email = '' if doc['anonymous'] else doc['_id']
            entries.append(LeaderboardEntry(username=email, score=doc['result'], score_type=type, version='demo',
                                            date=doc['date']))

        return entries

    # TODO move to own repo
    async def find_by_limits(self, page: int, per_page: int) -> list[LeaderboardEntry]:
        entries = []
        skip_count = per_page * (page - 1)

        cursor = self.collection.aggregate([
            {'$sort': {'result': 1}},
            {'$group': {
                '_id': {'user_email': '$user_email', 'type': '$type'},
                'result': {'$first': '$result'},
                'date': {'$first': '$date'},
                'anonymous': {'$first': '$anonymous'}
            }},
            {'$skip': skip_count},
            {'$limit': per_page}
        ])

        for doc in await cursor.to_list(length=None):
            email = '' if doc['anonymous'] else doc['_id']['user_email']
            entries.append(
                LeaderboardEntry(username=email, score=doc['result'], score_type=doc['_id']['type'], version='demo',
                                 date=doc['date']))

        return entries

    async def get_size(self) -> int:
        cursor = self.collection.aggregate([
            {'$group': {
                '_id': {'user_email': '$user_email', 'type': '$type'}
            }},
            {'$count': 'count'}
        ])

        async for doc in cursor:
            count = doc['count']

        return count if count else 0

    async def get_all_types(self) -> list[str]:
        return await self.collection.find({}, {'type': 1}).distinct('type')
