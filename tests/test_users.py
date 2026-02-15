from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def teste_creatte_user():
    response = client.post(
        "/users/",
        json={
            "id": 1,
            "name": "Vinicius",
            "email": "vinicius@email.com",
            "senha": "123456",
        },
    )

    assert response.status_code == 200
    assert response.json()["name"] == "Vinicius"
