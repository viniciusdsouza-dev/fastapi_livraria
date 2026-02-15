from fastapi import APIRouter, HTTPException
from app.models.models_cart import CartBase
from app.database import users, books, carts


router = APIRouter(prefix="/cart", tags=["Cart"])


@router.post("/add/{user_id}/{book_id}")
def add_to_cart(user_id: int, book_id: int):

    # Verifica se o usuário existe
    if not any(user.id == user_id for user in users):
        raise HTTPException(status_code=401, detail="Usuário não cadastrado")

    # Verifica se o livro existe
    if not any(book.id == book_id for book in books):
        raise HTTPException(status_code=404, detail="Livro não encontrado")

    # Procura o carrinho existente
    cart = next(
        (cart_item for cart_item in carts if cart_item.usuario_id == user_id), None
    )

    if cart:
        cart.books.append(book_id)
    else:
        cart = CartBase(usuario_id=user_id, books=[book_id])
        carts.append(cart)

    return {"message": "Livro adiciona ao carrinho"}
