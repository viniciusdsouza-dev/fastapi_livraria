from typing import List
from pydantic import BaseModel


# Modelo base para Usuarios
class UserCreate(BaseModel):
    name: str
    email: str
    senha: str
    

class User(UserCreate):
    id: int
