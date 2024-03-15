from motor.core import AgnosticDatabase, AgnosticCollection

from leaderboard.leaderboard_repo import LeaderboardRepo
from leaderboard.leaderboard_entry import LeaderboardEntry

class LeaderboardMongo(LeaderboardRepo):
    def __init__(self, mongo_database: AgnosticDatabase):
        self.leaderboard_collection: AgnosticCollection = mongo_database['leaderboard']

    async def find_all(self) -> list[LeaderboardEntry]:
        pass

    async def find_by_type(self, type: str) -> list[LeaderboardEntry]:
        pass