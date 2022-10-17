from typing import List
from ..infra.session import UserSession
from ..schemas.user_schema import User, UserCreate, UserUpdate
from ..service.user_service import UserService

class UserController():

    def __init__(self, session: UserSession) -> None:
        self._user_service = UserService(session)

    def new_user(self, user: UserCreate):
        self._user_service.new(user)

    def get_users(self) -> List[User]:
        return self._user_service.get_list()

    def get_user_by_id(self, id: int) -> User:
        return self._user_service.get_by_id(id)

    def update_user(self, id: int, user: UserUpdate):
        self._user_service.update(id, user)

    def delete_user(self, id: int):
        self._user_service.delete(id)