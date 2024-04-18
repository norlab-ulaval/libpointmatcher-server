from motor.core import AgnosticDatabase, AgnosticCollection

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
    return LeaderboardEntry(json['file_name'], json['type'], json['user_email'], json['rotation_error'],
                            json['translation_error'], json['date'], json['release_version'])


class LeaderboardMongo(LeaderboardRepo):
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
