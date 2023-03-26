from typing import List
from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str


class UserResponse(BaseModel):
    id: int
    usename: str
    is_admin: bool

    class Config:
        orm_mode = True