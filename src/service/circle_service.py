from typing import List
from repositories.circle_repository import CircleRepository
from schemas.circle import Circle, CircleCreate

class CircleService():
    
    def __init__(self) -> None:
        self._circle_repository = CircleRepository()

    def save(self, circle: CircleCreate):
        self._circle_repository.add(circle)

    def get_all(self) -> List[Circle]:
        return self._circle_repository.get_all()

    def find(self, id: int) -> Circle:
        return self._circle_repository.find(id)