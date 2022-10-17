class UserRepositoy:
    def __init__(self, session: Session) -> None:
        self._session = session

    def add(self, user: UserCreate):
        try:
            user_db = User(name = user.name)
            self._session.add(user_db)
            self._session.commit()
        except Exception:
            raise Exception

    def get_all(self) -> List[User]:
        pass

    def find(id: int) -> User:
        pass

    def update(id: int, user: UserUpdate):
        pass

    def delete(id: int):
        pass