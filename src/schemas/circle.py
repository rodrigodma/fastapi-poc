from pydantic import BaseModel

class CircleBase(BaseModel):
    radial: int

class Circle(CircleBase):
    id: int

    class Config:
        orm_mode = True