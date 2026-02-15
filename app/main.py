from typing import Dict
from fastapi import FastAPI
from app.routers import routers_books, routers_cart, routers_user


MESSAGE_HOME: str = "Bem-vindo à API da livraria Oráculo"

# Criando o App
app = FastAPI()

app.include_router(routers_books.router)
app.include_router(routers_user.router)
app.include_router(routers_cart.router)


@app.get("/")
def home() -> Dict[str, str]:
    global MESSAGE_HOME
    return {"mensagem": MESSAGE_HOME}
