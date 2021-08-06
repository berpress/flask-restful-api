import requests

base_url = "http://127.0.0.1:5000"

# create user
print("create user")
payload_register = {"username": "test11", "password": "Password11"}
response_register = requests.request(
    "POST", base_url + "/register", json=payload_register
)
user_id = response_register.json().get("uuid")
print(response_register.text)
print("____________________")

# get user tokens
print("get user tokens")
response_auth = requests.request("POST", base_url + "/auth", json=payload_register)
token = response_auth.json()["access_token"]
print(response_auth.text)
print("____________________")


# create store
print("create store")
response_store = requests.request(
    "POST", base_url + "/store/cars", headers={"Authorization": f"JWT {token}"}
)
print(response_store.text)
print("____________________")


# create items
print("create items")
payload_item = {"price": 2000, "store_id": 1}
response_items = requests.request(
    "POST",
    base_url + "/item/bmw",
    json=payload_item,
    headers={"Authorization": f"JWT {token}"},
)
print(response_items.text)
print("____________________")


payload_item = {"price": 1000, "store_id": 1}
response_items = requests.request(
    "POST",
    base_url + "/item/lada",
    json=payload_item,
    headers={"Authorization": f"JWT {token}"},
)
print(response_items.text)
print("____________________")


# change item
print("change items")
payload_item = {"price": 1947, "store_id": 1}
response_change_items = requests.request(
    "PUT",
    base_url + "/item/lada",
    json=payload_item,
    headers={"Authorization": f"JWT {token}"},
)
print(response_change_items.text)
print("____________________")


# get item
print("get item")
response_get_item = requests.request(
    "GET", base_url + "/item/lada", headers={"Authorization": f"JWT {token}"}
)
print(response_get_item.text)
print("____________________")


# get items
print("get items")
response_get_items = requests.request("GET", base_url + "/items")
print(response_get_items.text)
print("____________________")


# delete items
print("delete items")
response_delete_item = requests.request(
    "DELETE", base_url + "/item/bmw", headers={"Authorization": f"JWT {token}"}
)
print(response_delete_item.text)
print("____________________")


response_delete_item = requests.request(
    "DELETE", base_url + "/item/lada", headers={"Authorization": f"JWT {token}"}
)
print(response_delete_item.text)
print("____________________")


# get items
print("get items")
response_get_items = requests.request("GET", base_url + "/items")
print(response_get_items.text)
print("____________________")


# get balance
print("get balance")
response_get_balance = requests.request(
    "GET",
    base_url + "/balance/" + str(user_id),
    headers={"Authorization": f"JWT {token}"},
)
print(response_get_balance.text)
print("____________________")


# add balance
print("add balance")
payload_balance = {"balance": 1000}
response_add_balance = requests.request(
    "POST",
    base_url + "/balance/" + str(user_id),
    headers={"Authorization": f"JWT {token}"},
    json=payload_balance,
)
print(response_add_balance.text)
print("____________________")

# get balance
print("get balance")
response_get_balance = requests.request(
    "GET",
    base_url + "/balance/" + str(user_id),
    headers={"Authorization": f"JWT {token}"},
)
print(response_get_balance.text)
print("____________________")


# create items
print("create items")
payload_item = {"price": 1400, "store_id": 1}
response_items = requests.request(
    "POST",
    base_url + "/item/bmw",
    json=payload_item,
    headers={"Authorization": f"JWT {token}"},
)
print(response_items.text)
print("____________________")

# pay items
print("pay items")
payload_item = {"itemId": 1}
response_items = requests.request(
    "POST",
    base_url + "/pay/1",
    json=payload_item,
    headers={"Authorization": f"JWT {token}"},
)
print(response_items.text)
print("____________________")

# get balance
print("get balance")
response_get_balance = requests.request(
    "GET",
    base_url + "/balance/" + str(user_id),
    headers={"Authorization": f"JWT {token}"},
)
print(response_get_balance.text)
print("____________________")
