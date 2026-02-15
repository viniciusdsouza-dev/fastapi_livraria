from typing import List
from fastapi import APIRouter, HTTPException
from app.models.models_user import User, UserCreate
from app.database import users


router = APIRouter(prefix="/users", tags=["Users"])

user_id_counter = 1


@router.post("/", response_model=User)
def create_user(user: UserCreate):
    """
    Cria um novo Usuário.
    
    Args:
        usuário (UserCreate): O objeto contendo os dados do usuário criado
        
    Returns
        lusuário: O objeto do usuário recém-criado com um ID gerado.
    """
    global user_id_counter

    new_user = User(id=user_id_counter, **user.model_dump())
    users.append(new_user)
    user_id_counter += 1

    return new_user


@router.get("/", response_model=List[User])
def list_users():
    """
    Lista todos os usuários cadastrados.
    
    Returns:
        List[User]: Uma lista de objetos de usuários cadastrados.
    """
    return users
