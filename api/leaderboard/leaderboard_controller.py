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

    async def get_leaderboard(self, page: int, limit: int, type: Optional[str] = None) -> Leaderboard:
        # Hardcoded data for demo
        mock_data = [
            LeaderboardEntry(date='2024-02-11', version='1.0.0', username='Anonymous', score=99, score_type='Average'),
            LeaderboardEntry(date='2024-01-02', version='1.8.6', username='Anonymous', score=98, score_type='Average'),
            LeaderboardEntry(date='2023-12-28', version='1.9.6', username='XYZ Robotics', score=97.8, score_type='Average'),
            LeaderboardEntry(date='2023-12-14', version='1.8.3', username='Gamma Industries', score=97.4, score_type='Average'),
            LeaderboardEntry(date='2023-11-01', version='1.9.0', username='Beta Solutions', score=96.9, score_type='Average'),
            LeaderboardEntry(date='2023-10-21', version='1.3.8', username='Anonymous', score=96.1, score_type='Average'),
            LeaderboardEntry(date='2023-10-06', version='1.1.3', username='Alpha tech', score=94, score_type='Average'),
            LeaderboardEntry(date='2023-04-02', version='1.8.1', username='John doe', score=92, score_type='Average'),
            LeaderboardEntry(date='2023-03-14', version='1.3.7', username='Delta research', score=89, score_type='Average'),
            LeaderboardEntry(date='2023-03-14', version='1.3.7', username='Delta research', score=89, score_type='Average')
        ]

        # if type is not None and type != "all":
        #     leaderboard = await self._find_by_type(type)
        # else:
        #     leaderboard = await self._find_all()

        # if leaderboard:
        #     sorted_leaderboard = self.rank_leaderboard(leaderboard)
        # else:
        #     raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
        #                         detail="Error loading the leaderboard")

        # start_index = (page - 1) * limit
        # end_index = start_index + limit
        # size = await self._get_leaderboard_size()

        # leaderboard = Leaderboard(sorted_leaderboard[start_index:end_index], size)
        # return leaderboard
        mock_leaderboard = Leaderboard(entries=mock_data, total=len(mock_data))
        return mock_leaderboard

    def rank_leaderboard(self, leaderboard: list[LeaderboardEntry]) -> list[LeaderboardEntry]:
        sorted_leaderboard = sorted(leaderboard, key=lambda x: x.score, reverse=True)
        # If we want to rank it, for example to save it
        # for rank, entry in enumerate(sorted_leaderboard, start=1):
        #     entry.rank = rank
        return sorted_leaderboard
