from fastapi.testclient import TestClient
from app.main import app
from app.database import SessionLocal, engine

app.dependency_overrides[get_db] = override_get_db

def override_get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def test_create_book():
    client = TestClient(app)
    response = client.post(
        "/books/",
        json={"title": "Test Book", "author_id": 1},
    )
    assert response.status_code == 200
    assert response.json()["title"] == "Test Book"
    assert response.json()["author_id"] == 1

