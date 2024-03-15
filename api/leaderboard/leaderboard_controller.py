from interface.interface_models import Leaderboard
from leaderboard.leaderboard_repo import LeaderboardRepo


class LeaderboardController:
    def __init__(self, leaderboard_repo: LeaderboardRepo):
        self.leaderboard_repo = leaderboard_repo

    def get_leaderboard(self, page: int, limit: int, type: str) -> Leaderboard:
        pass
