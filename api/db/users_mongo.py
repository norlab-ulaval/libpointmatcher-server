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
