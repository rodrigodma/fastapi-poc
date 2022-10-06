from ..infra.db import SessionLocal
from ..infra.session import CircleSession
    
def get_session() -> CircleSession:
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()