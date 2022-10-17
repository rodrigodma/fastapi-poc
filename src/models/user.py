from sqlalchemy import Column, Integer, Text
from ..infra.db import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text, nullable=False)