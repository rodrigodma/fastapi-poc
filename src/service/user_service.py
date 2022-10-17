from typing import List
from ..infra.session import UserSession
from ..repositories.user_repository import UserRepositoy
from ..schemas.user_schema import User, UserCreate, UserUpdate


class UserService():

    def __init__(self, session: UserSession) -> None:
        self._user_repository = UserRepositoy(session)

    def new(self, user: UserCreate):
        self._user_repository.add(user)

    def get_list(self) -> List[User]:
        return self._user_repository.get_all()

    def get_by_id(self, id: int) -> User:
        return self._user_repository.find(id)

    def update(self, id: int, user: UserUpdate):
        self._user_repository.update(id, user)

    def delete(self, id: int):
        self._user_repository.delete(id)