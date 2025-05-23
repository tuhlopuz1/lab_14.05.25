from pydantic import BaseModel, UUID4, Field
from typing import Optional, Literal
from enum import Enum



class Role(str, Enum):
    USER = 'USER'
    ADMIN = 'ADMIN'

class UserLogin(BaseModel):
    username: str
    password: str

class UserCreate(BaseModel):
    username: str
    password: str
    role: Role

class Tokens(BaseModel):
    access_token: str
    refresh_token: str

class UserResponse(BaseModel):
    id: int
    username: str
    hashed_password: str
    role: Role