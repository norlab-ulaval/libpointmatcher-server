from pydantic import BaseModel
from datetime import datetime

class LeaderboardEntry(BaseModel):
    username: str
    score: float
    score_type: str
    version: str
    date: datetime
