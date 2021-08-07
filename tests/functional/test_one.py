class TestOne:
    def test_one(self, client):
        base_url = "http://127.0.0.1:5000"
        payload_register = {"username": "test111", "password": "Password111"}
        response = client.get(url=base_url + "/register", json=payload_register)
        assert response.status_code == 200
