from interface.interface_models import Leaderboard
from leaderboard.leaderboard_entry import LeaderboardEntry, LeaderboardEntryOld
from leaderboard.leaderboard_repo import LeaderboardRepo
from typing import Optional, List
from fastapi import HTTPException, status


class LeaderboardController:
    def __init__(self, leaderboard_repo: LeaderboardRepo):
        self.leaderboard_repo = leaderboard_repo

    async def _find_by_type(self, type: str, page: int, limit: int):
        return await self.leaderboard_repo.find_by_type_and_limits(type, page, limit)

    async def _find_all(self, page: int, limit: int):
        return await self.leaderboard_repo.find_by_limits(page, limit)

    async def _get_leaderboard_size(self) -> int:
        return await self.leaderboard_repo.get_size()

    async def get_leaderboard(self, page: int, limit: int, type: Optional[str] = None) -> Leaderboard:
        if type is not None and type != "all":
            leaderboard = await self._find_by_type(type, page, limit)
        else:
            leaderboard = await self._find_all(page, limit)

        leaderboard_old = self.convert_entries_to_old(leaderboard)

        size = await self._get_leaderboard_size()

        leaderboard_response = Leaderboard(entries=leaderboard_old, total=size)

        return leaderboard_response

    async def get_all_types(self) -> list[str]:
        return await self.leaderboard_repo.get_all_types()

    def convert_entries_to_old(self, entries: list[LeaderboardEntry]) -> list[LeaderboardEntryOld]:
        entries_old = []

        for e in entries:
            entries_old.append(LeaderboardEntryOld(e.user_email, e.rotation_error, e.type, e.release_version, e.date))

        return entries_old
