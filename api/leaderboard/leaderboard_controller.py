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

    async def get_leaderboard(self, page: int, limit: int, type: Optional[str] = None) -> list[LeaderboardEntry]:
        if type:
            leaderboard = await self._find_by_type(type)
        else:
            leaderboard = await self._find_all()

        sorted_leaderboard = self.rank_leaderboard(leaderboard)

        start_index = (page - 1) * limit
        end_index = start_index + limit

        return sorted_leaderboard[start_index:end_index]

    async def post_entry(self, entry: LeaderboardEntry):
        # TODO: Validation, and maybe make sure that the sender is the website?
        try:
            await self.leaderboard_repo.add_one(entry)
        except:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="Could not logout user")

    def rank_leaderboard(self, leaderboard: list[LeaderboardEntry]) -> list[LeaderboardEntry]:
        sorted_leaderboard = sorted(leaderboard, key=lambda x: x.score, reverse=True)
        # If we want to rank it, for example to save it
        # for rank, entry in enumerate(sorted_leaderboard, start=1):
        #     entry.rank = rank
        return sorted_leaderboard
