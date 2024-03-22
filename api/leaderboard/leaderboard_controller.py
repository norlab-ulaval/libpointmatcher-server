from interface.interface_models import Leaderboard, LeaderboardEntry
from leaderboard.leaderboard_repo import LeaderboardRepo
from typing import Optional
from fastapi import HTTPException, status


class LeaderboardController:
    def __init__(self, leaderboard_repo: LeaderboardRepo):
        self.leaderboard_repo = leaderboard_repo

    async def _find_by_type(self, type: str):
        return await self.leaderboard_repo.find_by_type(type)

    async def _find_all(self):
        return await self.leaderboard_repo.find_all()

    async def _get_leaderboard_size(self):
        return await self.leaderboard_repo.get_size()

    async def get_leaderboard(self, page: int, limit: int, type: Optional[str] = None) -> list[LeaderboardEntry]:
        if type is not None and type != "all":
            leaderboard = await self._find_by_type(type)
        else:
            leaderboard = await self._find_all()

        if leaderboard:
            sorted_leaderboard = self.rank_leaderboard(leaderboard)
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="Error loading the leaderboard")

        start_index = (page - 1) * limit
        end_index = start_index + limit
        size = await self._get_leaderboard_size()

        leaderboard = Leaderboard(sorted_leaderboard[start_index:end_index], size)
        return leaderboard

    def rank_leaderboard(self, leaderboard: list[LeaderboardEntry]) -> list[LeaderboardEntry]:
        sorted_leaderboard = sorted(leaderboard, key=lambda x: x.score, reverse=True)
        # If we want to rank it, for example to save it
        # for rank, entry in enumerate(sorted_leaderboard, start=1):
        #     entry.rank = rank
        return sorted_leaderboard

    async def get_all_types(self) -> list[str]:
        return await self.leaderboard_repo.get_all_types()
