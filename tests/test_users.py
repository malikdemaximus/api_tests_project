from utils.api_helpers import get_user, create_user

def test_get_existing_user(base_url):
    response = get_user(base_url, 2)
    assert response.status_code == 200
    assert response.json()["data"]["id"] == 2

def test_get_non_existing_user(base_url):
    response = get_user(base_url, 999)
    assert response.status_code == 404

def test_create_user(base_url):
    data = {
        "name": "Ali",
        "job": "tester"
    }
    response = create_user(base_url, data)
    assert response.status_code == 201
    assert response.json()["name"] == "Ali"
