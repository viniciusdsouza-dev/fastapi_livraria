from typing import List
from pydantic import BaseModel


# Modelo base para livros
class BooksCreate(BaseModel):
    title: str
    author: str
    price: float
    tags: List[str]
    

class Book(BooksCreate):
    id: int
