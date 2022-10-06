from pydantic import BaseModel
from sqlalchemy import Column, Integer

from ..infra.db import Base

class Circle(Base):
    __tablename__ = 'circles'
    id = Column(Integer, primary_key=True, index=True)
    radial = Column(Integer, nullable=False)