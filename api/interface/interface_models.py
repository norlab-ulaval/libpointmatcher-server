from pydantic import BaseModel, Field

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None
    email: str | None = None

class RegisteringUser(BaseModel):
    username: str
    email: str
    password: str

class LoginUser(BaseModel):
    username: str
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
    
class LeaderboardEntry(BaseModel):
    username: str
    score: int
    version: str
    date: str

class Leaderboard(BaseModel):
    entries: list[LeaderboardEntry] = Field(default_factory=list)
    total: int