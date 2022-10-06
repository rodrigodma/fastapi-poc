from typing import List
from sqlalchemy.orm import Session

from models.circle import Circle
from schemas.circle import Circle, CircleCreate

class CircleRepository:
    def __init__(self, session: Session) -> None:
        self._session =  session

    def add(self, circle: CircleCreate):
        try:
            circle_db = Circle(radial=circle.radial)
            self._session.add(circle_db)
            self._session.commit()
        except Exception:
            raise Exception

    def get_all() -> List[Circle]:
        pass

    def find(id: int) -> Circle:
        pass