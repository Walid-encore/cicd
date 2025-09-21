from fastapi.testclient import TestClient
from src.main import api  # import your FastAPI instance

client = TestClient(api)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_post_todo():
    todo_data = {"id": 1, "name": "Test TODO", "descripton": "Testing"}  # note typo matches your model
    response = client.post("/todo", json=todo_data)
    assert response.status_code == 200
    assert response.json() == [todo_data]

def test_get_todo():
    response = client.get("/todo")
    assert response.status_code == 200
    assert len(response.json()) >= 1  # At least 1 todo

def test_update_todo():
    updated_data = {"id": 1, "name": "Updated TODO", "descripton": "Updated description"}
    response = client.put("/todo/1", json=updated_data)
    assert response.status_code == 200
    assert response.json()[0]["name"] == "Updated TODO"

def test_delete_todo():
    response = client.delete("/todo/1")
    assert response.status_code == 200
    assert response.json() == []