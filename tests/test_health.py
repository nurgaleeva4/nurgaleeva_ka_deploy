import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def test_health_endpoint(client):
    """Тест эндпоинта /health"""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "environment" in data
    assert "version" in data

def test_root_endpoint_with_environment(client):
    """Тест корневого эндпоинта с окружением"""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "environment" in data
    assert "app_name" in data