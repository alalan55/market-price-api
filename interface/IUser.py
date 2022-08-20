from pydantic import BaseModel


class UserBase(BaseModel):
    name: str


class UserCrete(UserBase):
    ...
class User(UserBase):
    id: int
    class Config:
        orm_mode = True
