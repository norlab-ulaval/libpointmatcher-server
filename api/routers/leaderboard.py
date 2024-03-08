from fastapi import APIRouter

from interface.interface_models import Leaderboard, LeaderboardQuery, LeaderboardEntry
from leaderboard.leaderboard_controller import LeaderboardController

leaderboard_controller: LeaderboardController

router = APIRouter()


@router.get("/leaderboard", response_model=Leaderboard)
async def get_leaderboard(query: LeaderboardQuery):
    return await leaderboard_controller.get_leaderboard(query.page, query.limit, query.type)


@router.post("/leaderboard/entry")
async def post_leaderboard_entry(entry: LeaderboardEntry):
    return await leaderboard_controller.post_entry(entry)
