def test_square(client):
    payload_register = {"username": "test111", "password": "Password111"}
    rv = client.post("/register", json=payload_register)
    assert rv.status_code == 201
