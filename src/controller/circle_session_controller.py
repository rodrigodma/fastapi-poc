from infra.db import SessionLocal
from infra.session import CircleSession

class CircleSessionController():

    def __init__(self) -> None:
        pass
    
    def get_session() -> CircleSession:
        session = SessionLocal()
        try:
            yield session
        finally:
            session.close()