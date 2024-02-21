from user.user import User


class UserRepo:
    async def find_all(self) -> list[User]:
        pass

    async def find(self, username: str, password: str) -> User:
        pass

    async def find_username(self, username: str) -> User:
        pass

    async def find_email(self, email: str) -> User:
        pass

    async def add_user(self, username: str, email: str, password: str) -> User:
        pass

    async def does_user_exist(self, username=None, email=None) -> bool:
        pass
