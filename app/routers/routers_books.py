from typing import List
from fastapi import APIRouter, HTTPException
from app.models.models_books import Book, BooksCreate
from app.database import books

router = APIRouter(prefix="/books", tags=["Books"])

book_id_counter = 1


@router.post("/", response_model=Book)
def create_book(book: BooksCreate):
    """
    Cria um novo livro.
    
    Args:
        livro (BooksCreate): O objeto contendo os dados do livro criado
        
    Returns
        livro: O objeto do livro recém-criado com um ID gerado.
    """
    global book_id_counter

    new_book = Book(id=book_id_counter, **book.model_dump())
    books.append(new_book)
    book_id_counter += 1

    return new_book


@router.get("/", response_model=List[Book])
def list_books():
    """
    Lista todos os livros cadastrados.
    
    Returns:
        List[Book]: Uma lista de objetos de livros cadastrados.
    """
    return books
