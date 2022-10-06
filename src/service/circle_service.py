from typing import List
from infra.session import CircleSession
from repositories.circle_repository import CircleRepository
from schemas.circle import Circle, CircleCreate

class CircleService():
    
    def __init__(self, session: CircleSession) -> None:
        self._circle_repository = CircleRepository(session)

    def save(self, circle: CircleCreate):
        self._circle_repository.add(circle)

    def get_all(self) -> List[Circle]:
        return self._circle_repository.get_all()

    def find(self, id: int) -> Circle:
        return self._circle_repository.find(id)