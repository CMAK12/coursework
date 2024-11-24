from fastapi.testclient import TestClient

import db.database
from main import app

client = TestClient(app)

# def test_create_news(): # Temporary commented because of outdated code
#     response = client.post("/api/news/", json={
#         "title": "Test News",
#         "author": "Author Name",
#         "description": "A description",
#         "published_year": 2023
#     })
#     assert response.status_code == 200
#     assert response.json()["title"] == "Test News"

def test_is_database_singlton():
    db1 = db.database.database.__hash__()
    db2 = db.database.database.__hash__()
    assert db1 == db2