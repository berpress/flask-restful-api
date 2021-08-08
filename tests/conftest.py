# Third party modules
import pytest

# First party modules
from app2 import create_app


@pytest.fixture
def client():
    app = create_app()
    from db import db

    db.init_app(app)

    @app.before_first_request
    def create_tables():
        db.create_all()

    app.config["TESTING"] = True
    app.config["DEBUG"] = True
    with app.test_client() as client:
        yield client
