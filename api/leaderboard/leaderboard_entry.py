from pydantic import BaseModel
from datetime import datetime


class LeaderboardEntry(BaseModel):
    file_name: str
    type: str
    user_email: str
    rotation_error: float
    translation_error: float
    date: datetime
    release_version: str
