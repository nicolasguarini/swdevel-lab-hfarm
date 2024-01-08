import os
import sys
from fastapi.testclient import TestClient
import json
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')
))
from app.main import app


client = TestClient(app)


def test_advanced_search_wines_by_type():
    response = client.get("/advanced-search", params={
        "limit": 5,
        "type": "red"
    })

    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"

    wines = json.loads(response.text)
    assert isinstance(wines, list)
    assert all(isinstance(wine, dict) for wine in wines)


def test_advanced_search_wines_by_year():
    response = client.get("/advanced-search", params={
        "limit": 5,
        "year_start": 2012,
        "year_end": 2015
    })

    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"

    wines = json.loads(response.text)
    assert isinstance(wines, list)
    assert all(isinstance(wine, dict) for wine in wines)
