from leaderboard.leaderboard_entry import LeaderboardEntry


class LeaderboardRepo:
    async def find_all(self) -> list[LeaderboardEntry]:
        pass

    async def find_by_type(self, type: str) -> list[LeaderboardEntry]:
        pass

    async def get_all_types(self) -> list[str]:
        pass
