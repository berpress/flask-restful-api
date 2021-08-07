import requests

import pytest


@pytest.fixture(scope="session")
def client():
    client = requests.session()
    yield client
