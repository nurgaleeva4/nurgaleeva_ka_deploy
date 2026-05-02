import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def test_create_item(client):
    response = client.post("/items/", json={"name": "Laptop", "price": 999.99})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Laptop"
    assert data["price"] == 999.99
    assert "id" in data


def test_get_item_not_found(client):
    response = client.get("/items/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Item not found"


def test_create_and_get_item(client):
    create_response = client.post("/items/", json={"name": "Mouse", "price": 29.99})
    assert create_response.status_code == 200
    item_id = create_response.json()["id"]

    get_response = client.get(f"/items/{item_id}")
    assert get_response.status_code == 200
    assert get_response.json()["name"] == "Mouse"