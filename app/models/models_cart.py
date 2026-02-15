from typing import List
from pydantic import BaseModel


class CartBase(BaseModel):
    usuario_id: int
    books: List[int]
