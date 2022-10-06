from typing import List
from schemas.circle import Circle, CircleCreate
from service.circle_service import CircleService

class CircleController():

    def __init__(self) -> None:
        self._circle_service = CircleService()

    def save(self, circle: CircleCreate):
        self._circle_service.save(circle)

    def get_all(self) -> List[Circle]:
        return self._circle_service.get_all()

    def find(self, id: int) -> Circle:
        return self._circle_service.find(id)