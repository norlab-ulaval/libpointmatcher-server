from api.user.user import User
from api.user.user_repo import UserRepo


class UserController:
    def __init__(self, user_repo: UserRepo):
        self.user_repo = user_repo

    async def get_all_users(self) -> list[User]:
        return await self.user_repo.find_all()
