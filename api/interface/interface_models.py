from pydantic import BaseModel, Field
from leaderboard.leaderboard_entry import LeaderboardEntry, LeaderboardEntryOld


class Token(BaseModel):
    access_token: str
    token_type: str

class RegisteringUser(BaseModel):
    username: str
    email: str
    password: str

class LoginUser(BaseModel):
    email: str
    password: str

class User(BaseModel):
    username: str or None = None
    email: str

class UserInDB(User):
    hashed_password: str
    # yaml configs??

class LeaderboardQuery(BaseModel):
    page: int = 1
    limit: int = 10
    type: str = "all"


class Leaderboard:
    def __init__(self, entries: list[LeaderboardEntry], total: int):
        self.entries = entries
        self.total = total