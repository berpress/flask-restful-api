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


def test_add_user_information(client):
    payload_register = payload
    response = client.post("/auth", json=payload_register)
    assert response.status_code == 200
    token = response.json.get("access_token")
    payload_info = {
        "phone": "122434",
        "email": "test@test.com",
        "address": {"city": "Kazan", "street": "Prospect pobedy", "home_number": "12"},
    }
    response = client.post(
        "/user_info/1", json=payload_info, headers={"Authorization": f"JWT {token}"}
    )
    assert response.status_code == 200
    assert response.json.get("message") == "User info created successfully."


def test_add_user_information_invalid_user(client):
    payload_register = payload
    response = client.post("/auth", json=payload_register)
    assert response.status_code == 200
    token = response.json.get("access_token")
    payload_info = {
        "phone": "122434",
        "email": "test@test.com",
        "address": {"city": "Kazan", "street": "Prospect pobedy", "home_number": "12"},
    }
    response = client.post(
        "/user_info/10000", json=payload_info, headers={"Authorization": f"JWT {token}"}
    )
    assert response.status_code == 404
    assert response.json.get("message") == "User not found"


def test_path_user_information(client):
    payload_register = payload
    response = client.post("/auth", json=payload_register)
    assert response.status_code == 200
    token = response.json.get("access_token")
    payload_info = {
        "phone": "77777",
        "email": "name@test.com",
        "address": {"city": "NY", "street": "Louge street", "home_number": "209"},
    }
    response = client.put(
        "/user_info/1", json=payload_info, headers={"Authorization": f"JWT {token}"}
    )
    assert response.status_code == 200
    assert response.json.get("message") == "User info updated successfully."


def test_path_user_information_invalid_user(client):
    payload_register = payload
    response = client.post("/auth", json=payload_register)
    assert response.status_code == 200
    token = response.json.get("access_token")
    payload_info = {
        "phone": "77777",
        "email": "name@test.com",
        "address": {"city": "NY", "street": "Louge street", "home_number": "209"},
    }
    response = client.put(
        "/user_info/10000", json=payload_info, headers={"Authorization": f"JWT {token}"}
    )
    assert response.status_code == 404
    assert response.json.get("message") == "User info not found."


def test_get_user_information(client):
    payload_register = payload
    response = client.post("/auth", json=payload_register)
    assert response.status_code == 200
    token = response.json.get("access_token")
    response = client.get("/user_info/1", headers={"Authorization": f"JWT {token}"})
    assert response.status_code == 200


def test_get_user_information_invalid_user(client):
    payload_register = payload
    response = client.post("/auth", json=payload_register)
    assert response.status_code == 200
    token = response.json.get("access_token")
    response = client.get(
        "/user_info/100000", headers={"Authorization": f"JWT {token}"}
    )
    assert response.status_code == 404
    assert response.json.get("message") == "User info not found"


def test_add_store(client):
    payload_register = payload
    response = client.post("/auth", json=payload_register)
    assert response.status_code == 200
    token = response.json.get("access_token")
    response = client.post("/store/cars", headers={"Authorization": f"JWT {token}"})
    assert response.status_code == 201
    assert response.json.get("name") == "cars"
    assert len(response.json.get("items")) == 0


def test_add_store_twice(client):
    payload_register = payload
    response = client.post("/auth", json=payload_register)
    assert response.status_code == 200
    token = response.json.get("access_token")
    response = client.post("/store/cars", headers={"Authorization": f"JWT {token}"})
    assert response.status_code == 400


def test_add_items(client):
    payload_register = payload
    response = client.post("/auth", json=payload_register)
    assert response.status_code == 200
    token = response.json.get("access_token")
    payload_item = {"price": 2000, "store_id": 1}
    response = client.post(
        "/item/bmw", headers={"Authorization": f"JWT {token}"}, json=payload_item
    )
    assert response.status_code == 201
    assert response.json.get("name") == "bmw"
    assert response.json.get("price") == 2000.0


def test_change_items(client):
    payload_register = payload
    response = client.post("/auth", json=payload_register)
    assert response.status_code == 200
    token = response.json.get("access_token")
    payload_item = {"price": 1947, "store_id": 1}
    response = client.put(
        "/item/bmw", headers={"Authorization": f"JWT {token}"}, json=payload_item
    )
    assert response.status_code == 200
    assert response.json.get("name") == "bmw"
    assert response.json.get("price") == 1947.0


def test_get_items(client):
    payload_register = payload
    response = client.post("/auth", json=payload_register)
    assert response.status_code == 200
    token = response.json.get("access_token")
    response = client.get("/item/bmw", headers={"Authorization": f"JWT {token}"})
    assert response.status_code == 200
    assert response.json.get("name") == "bmw"
    assert response.json.get("price") == 1947.0


def test_get_all_items(client):
    payload_register = payload
    response = client.post("/auth", json=payload_register)
    assert response.status_code == 200
    token = response.json.get("access_token")
    response = client.get("/items", headers={"Authorization": f"JWT {token}"})
    assert response.status_code == 200


def test_add_balance(client):
    payload_register = payload
    response = client.post("/auth", json=payload_register)
    assert response.status_code == 200
    token = response.json.get("access_token")
    payload_balance = {"balance": 2000}
    response = client.post(
        "/balance/1", headers={"Authorization": f"JWT {token}"}, json=payload_balance
    )
    assert response.status_code == 201
    assert (
        response.json.get("message")
        == "User balance has been updated. New balance is 2000.0"
    )


def test_get_balance(client):
    payload_register = payload
    response = client.post("/auth", json=payload_register)
    assert response.status_code == 200
    token = response.json.get("access_token")
    response = client.get("/balance/1", headers={"Authorization": f"JWT {token}"})
    assert response.status_code == 200
    assert response.json.get("message") == "User balance is 2000.0"


def test_pay_item(client):
    payload_register = payload
    response = client.post("/auth", json=payload_register)
    assert response.status_code == 200
    token = response.json.get("access_token")
    payload_item = {"itemId": 1}
    response = client.post(
        "/pay/1", headers={"Authorization": f"JWT {token}"}, json=payload_item
    )
    assert response.status_code == 200
    assert response.json.get("message") == "Payment was successful"
    assert response.json.get("balance") == 53.0
    assert response.json.get("name") == "bmw"
    assert response.json.get("price") == 1947.0


def test_pay_item_not_enough_money(client):
    payload_register = payload
    response = client.post("/auth", json=payload_register)
    assert response.status_code == 200
    token = response.json.get("access_token")
    payload_item = {"itemId": 1}
    response = client.post(
        "/pay/1", headers={"Authorization": f"JWT {token}"}, json=payload_item
    )
    assert response.status_code == 400
    assert (
        response.json.get("message") == "Not enough money. Your balance is 53.0, "
        "item cost 1947.0"
    )
