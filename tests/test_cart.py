from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)



def test_add_to_cart():
    # Criar usuário
    client.post(
        "/users/",
        json={
            "id": 1,
            "name": "Vinicius",
            "email": "vinicius@email.com",
            "senha": "123456"
        }
    )

    # Criar livro
    client.post(
        "/books/",
        json={
            "id": 1,
            "title": "Clean Code",
            "author": "Robert C. Martin",
            "price": 99.9,
            "tags": ["programacao"]
        }
    )

    # Agora adicionar ao carrinho
    response = client.post("/cart/add/1/1")

    assert response.status_code == 200