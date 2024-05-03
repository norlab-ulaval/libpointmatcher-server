from fastapi import APIRouter

from interface.interface_models import Leaderboard, LeaderboardQuery, LeaderboardEntry
from leaderboard.leaderboard_controller import LeaderboardController

leaderboard_controller: LeaderboardController

router = APIRouter()


@router.get("/leaderboard", response_model=object)
async def get_leaderboard(page: int=1, limit: int=10, type: str="all"):
    return await leaderboard_controller.get_leaderboard(page, limit, type)


@router.get("/leaderboard/types", response_model=list[str])
async def get_all_types():
    return await leaderboard_controller.get_all_types()
