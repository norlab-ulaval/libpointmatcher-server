from pydantic import BaseModel, Field

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
    
class LeaderboardEntry(BaseModel):
    username: str
    score: int
    score_type: str
    version: str
    date: str

class Leaderboard(BaseModel):
    entries: list[LeaderboardEntry] = Field(default_factory=list)
    total: int