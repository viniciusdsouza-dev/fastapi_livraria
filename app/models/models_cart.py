from typing import List
from pydantic import BaseModel


# Modelo base para Carrinho
class CartBase(BaseModel):
    usuario_id: int
    books: List[int]
