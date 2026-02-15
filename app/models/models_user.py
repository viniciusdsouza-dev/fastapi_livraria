from typing import List
from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    email: str
    senha: str
    

class User(UserCreate):
    id: int
