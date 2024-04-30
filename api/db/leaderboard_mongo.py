from motor.core import AgnosticDatabase, AgnosticCollection

from evaluation.evaluation import Evaluation
from evaluation.new_evaluation_listener import NewEvaluationListener
from leaderboard.leaderboard_entry import LeaderboardEntry
from leaderboard.leaderboard_repo import LeaderboardRepo


def _to_json(entry: LeaderboardEntry):
    return {
        'file_name': entry.file_name,
        'type': entry.type,
        'user_email': entry.user_email,
        'rotation_error': entry.rotation_error,
        'translation_error': entry.translation_error,
        'date': entry.date,
        'release_version': entry.release_version
    }


def _from_json(json):
    return LeaderboardEntry(file_name = json['file_name'],
                            type = json['type'],
                            user_email = json['user_email'],
                            rotation_error = json['rotation_error'],
                            translation_error = json['translation_error'],
                            date = json['date'],
                            release_version = json['release_version'])


class LeaderboardMongo(LeaderboardRepo, NewEvaluationListener):
    def __init__(self, mongo_database: AgnosticDatabase):
        self.collection: AgnosticCollection = mongo_database['leaderboard']

    async def find_by_type(self, type: str) -> list[LeaderboardEntry]:
        entries = []

        cursor = self.collection.aggregate([
            {'$match': {'type': type}},
            {'$sort': {'rotation_error': 1}}
        ])

        for doc in await cursor.to_list(length=None):
            entries.append(_from_json(doc))

        return entries

    async def find_by_type_and_limits(self, type: str, page: int, per_page: int) -> list[LeaderboardEntry]:
        entries = []
        skip_count = per_page * (page - 1)

        cursor = self.collection.aggregate([
            {'$match': {'type': type}},
            {'$sort': {'rotation_error': 1}},
            {'$skip': skip_count},
            {'$limit': per_page}
        ])

        for doc in await cursor.to_list(length=None):
            entries.append(_from_json(doc))

        return entries

    async def find_by_limits(self, page: int, per_page: int) -> list[LeaderboardEntry]:
        entries = []
        skip_count = per_page * (page - 1)

        cursor = self.collection.aggregate([
            {'$sort': {'rotation_error': 1}},
            {'$skip': skip_count},
            {'$limit': per_page}
        ])

        for doc in await cursor.to_list(length=None):
            entries.append(_from_json(doc))

        return entries

    async def get_size(self) -> int:
        cursor = self.collection.aggregate([
            {'$count': 'count'}
        ])

        async for doc in cursor:
            count = doc['count']

        return count if count else 0

    async def get_all_types(self) -> list[str]:
        return await self.collection.find({}, {'type': 1}).distinct('type')

    async def notify_batch(self, evaluations: list[Evaluation]):
        for evaluation in evaluations:
            if evaluation.iterations:
                rotation_error = 0
                translation_error = 0

                for iteration in evaluation.iterations:
                    rotation_error = rotation_error + iteration.rotation_error
                    translation_error = translation_error + iteration.translation_error

                rotation_error = rotation_error / len(evaluation.iterations)
                translation_error = translation_error / len(evaluation.iterations)

                entry = LeaderboardEntry(file_name = evaluation.file_name,
                                         type = evaluation.type,
                                         user_email = evaluation.user_email,
                                         rotation_error = rotation_error,
                                         translation_error = translation_error,
                                         date = evaluation.date,
                                         release_version = "demo")

                doc = await self.collection.find_one({ 'file_name': entry.file_name,
                                                            'type': entry.type,
                                                            'user_email': entry.user_email},
                                                     {'rotation_error': 1, 'translation_error': 1})

                if doc:
                    if doc['rotation_error'] < entry.rotation_error:
                        entry.rotation_error = doc['rotation_error']
                    if doc['translation_error'] < entry.translation_error:
                        entry.translation_error = doc['translation_error']

                await self.collection.replace_one({'file_name': entry.file_name, 'type': entry.type, 'user_email': entry.user_email},
                                                  _to_json(entry), True)
