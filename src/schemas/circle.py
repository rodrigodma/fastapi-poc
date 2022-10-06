from pydantic import BaseModel

class CircleBase(BaseModel):
    radial: int

class CircleCreate(CircleBase):
    pass

class Circle(CircleBase):
    id: int

    class Config:
        orm_mode = True