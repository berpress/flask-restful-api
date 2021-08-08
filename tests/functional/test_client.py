USERNAME = "test111"
PASSWORD = "Password111"

payload = {"username": USERNAME, "password": PASSWORD}


def test_register_user(client):
    payload_register = payload
    response = client.post("/register", json=payload_register)
    assert response.status_code == 201
    assert response.json.get("message") == "User created successfully."
    assert response.json.get("uuid") is not None


def test_register_user_twice(client):
    payload_register = payload
    response = client.post("/register", json=payload_register)
    assert response.status_code == 400


def test_auth_user(client):
    payload_register = payload
    response = client.post("/auth", json=payload_register)
    assert response.status_code == 200
    assert response.json.get("access_token") is not None


def test_auth_user_invalid_data(client):
    payload_register = {"username": "test2", "password": "PASSWORD"}
    response = client.post("/auth", json=payload_register)
    assert response.status_code == 401
