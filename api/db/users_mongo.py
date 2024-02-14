from motor.core import AgnosticDatabase, AgnosticCollection

from user.user import User
from user.user_repo import UserRepo


class UsersMongo(UserRepo):
    def __init__(self, mongo_database: AgnosticDatabase):
        self.users_collection: AgnosticCollection = mongo_database['users']

    # TODO sample function only
    async def find_all(self) -> list[User]:
        cursor = self.users_collection.find()
        return await cursor.to_list(length=None)
    
    async def find(self, username: str, password: str) -> User:
        pass

    async def find_username(self, username: str) -> User:
        pass

    async def add_user(self, username: str, email: str, password: str) -> User:
        pass
