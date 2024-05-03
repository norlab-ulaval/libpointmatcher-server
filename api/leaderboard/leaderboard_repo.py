from leaderboard.leaderboard_entry import LeaderboardEntry


class LeaderboardRepo:
    async def find_by_type(self, type: str) -> list[LeaderboardEntry]:
        pass

    async def find_by_type_and_limits(self, type: str, page: int, per_page: int) -> list[LeaderboardEntry]:
        pass

    async def find_by_limits(self, page: int, per_page: int) -> list[LeaderboardEntry]:
        pass

    async def get_size(self) -> int:
        pass

    async def get_all_types(self) -> list[str]:
        pass
