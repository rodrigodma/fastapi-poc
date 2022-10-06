from sqlalchemy.orm import Session

from models.circle import Circle

class CircleRepository:
    def __init__(self, session: Session) -> None:
        self._session =  session

    def add(self, circle: Circle):
        try:
            self._session.add(circle)
            self._session.commit()
        except Exception:
            raise Exception