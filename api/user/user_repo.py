from user.user import User


class UserRepo:
    async def find_all(self) -> list[User]:
        pass

    async def find(self) -> User:
        pass

    async def find_username(self) -> User:
        pass

    async def add(self):
        pass
