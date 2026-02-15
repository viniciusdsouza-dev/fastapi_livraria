from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_creat_book():
    response = client.post(
        "/books/",
        json={
            "id": 1,
            "title": "Clean Code",
            "author": "Robert C. Martin",
            "price": 99.9,
            "tags": ["programacao", "boas praticas"],
        },
    )

    assert response.status_code == 200
    assert response.json()["title"] == "Clean Code"


def test_list_books():
    response = client.get("/books/")
    assert response.status_code == 200
