import pytest
from fastapi.testclient import TestClient
from app.main import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import get_db, Base
from app.models import User
from app.schemas import UserCreate

SQLALCHEMY_DATABASE_URL = "postgresql://user:password@localhost/test_db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="module")
def test_client():
    Base.metadata.create_all(bind=engine)
    yield TestClient(app)
    Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="function")
def db_session():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

def test_create_user(test_client, db_session):
    user_data = {"username": "testuser", "email": "test@example.com", "password": "testpassword"}
    response = test_client.post("/users/", json=user_data)
    assert response.status_code == 201
    assert response.json()["username"] == user_data["username"]

def test_read_user(test_client, db_session):
    user_data = {"username": "testuser", "email": "test@example.com", "password": "testpassword"}
    test_client.post("/users/", json=user_data)
    response = test_client.get("/users/testuser")
    assert response.status_code == 200
    assert response.json()["username"] == user_data["username"]

def test_update_user(test_client, db_session):
    user_data = {"username": "testuser", "email": "test@example.com", "password": "testpassword"}
    test_client.post("/users/", json=user_data)
    update_data = {"email": "updated@example.com"}
    response = test_client.put("/users/testuser", json=update_data)
    assert response.status_code == 200
    assert response.json()["email"] == update_data["email"]

def test_delete_user(test_client, db_session):
    user_data = {"username": "testuser", "email": "test@example.com", "password": "testpassword"}
    test_client.post("/users/", json=user_data)
    response = test_client.delete("/users/testuser")
    assert response.status_code == 204
    response = test_client.get("/users/testuser")
    assert response.status_code == 404

def test_integration_with_openai(test_client):
    response = test_client.post("/openai/generate", json={"prompt": "Hello, world!"})
    assert response.status_code == 200
    assert "generated_text" in response.json()

def test_frontend_rendering(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "Welcome" in response.text

def test_api_health_check(test_client):
    response = test_client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}