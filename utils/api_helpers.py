import requests

def get_user(base_url, user_id):
    return requests.get(f"{base_url}/users/{user_id}")

def create_user(base_url, data):
    return requests.post(f"{base_url}/users", json=data)
