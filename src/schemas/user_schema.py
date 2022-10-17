import string

from pydantic import BaseModel

class UserBase(BaseModel):
    name: string

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class User(UserBase):
    id: int

    class Config:
        orm_mode = True