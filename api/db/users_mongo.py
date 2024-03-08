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
    
    async def find(self, email: str, password: str) -> User:
        user_document = await self.users_collection.find_one({"email": email, "password": password})
        if user_document:
            return User(user_document["username"], user_document["email"], user_document["password"])
        return None

    async def find_username(self, username: str) -> User:
        user_document = await self.users_collection.find_one({"username": username})
        if user_document:
            return User(user_document["username"], user_document["email"], user_document["password"])
        return None
    
    async def find_email(self, email: str) -> User:
        user_document = await self.users_collection.find_one({"email": email})
        if user_document:
            return User(user_document["username"], user_document["email"], user_document["password"])
        return None

    async def does_user_exist(self, username=None, email=None) -> bool:
        user_username = await self.find_username(username) if username is not None else None
        user_email = await self.find_email(email) if email is not None else None

        return user_username is not None or user_email is not None

    async def add_user(self, username: str, email: str, password: str):
        user_json = {
            "username": username,
            "email": email,
            "password": password
        }
        await self.users_collection.insert_one(user_json)
