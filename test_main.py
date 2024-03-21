from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_get_student():
    response = client.get("/students")
    assert response.status_code == 200
    assert response.json() == {}


def test_create_student():
    response = client.post(
        "/students",
        headers={"Content-Type": "application/json"},
        json={"id": "9731025", "first_name": "elahe", "last_name": "dastan", "registration_date": "1396-07-01",
              "average": "18.1"},
    )
    assert response.status_code == 200
    assert response.json() == {'9731025': {'average': 18.1,
                                           'first_name': 'elahe',
                                           'graduation_date': None,
                                           'id': '9731025',
                                           'last_name': 'dastan',
                                           'registration_date': '1396-07-01'}}

# def test_read_item_bad_token():
#     response = client.get("/items/foo", headers={"X-Token": "hailhydra"})
#     assert response.status_code == 400
#     assert response.json() == {"detail": "Invalid X-Token header"}
#
#
# def test_read_nonexistent_item():
#     response = client.get("/items/baz", headers={"X-Token": "coneofsilence"})
#     assert response.status_code == 404
#     assert response.json() == {"detail": "Item not found"}
#
#

#
#
# def test_create_item_bad_token():
#     response = client.post(
#         "/items/",
#         headers={"X-Token": "hailhydra"},
#         json={"id": "bazz", "title": "Bazz", "description": "Drop the bazz"},
#     )
#     assert response.status_code == 400
#     assert response.json() == {"detail": "Invalid X-Token header"}
#
#
# def test_create_existing_item():
#     response = client.post(
#         "/items/",
#         headers={"X-Token": "coneofsilence"},
#         json={
#             "id": "foo",
#             "title": "The Foo ID Stealers",
#             "description": "There goes my stealer",
#         },
#     )
#     assert response.status_code == 409
#     assert response.json() == {"detail": "Item already exists"}
