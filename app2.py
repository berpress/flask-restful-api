# Third party modules
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from resources.balance import Balance
from resources.item import Item, ItemList
from resources.pay import Pay
from resources.store import Store, StoreList
from resources.user import UserRegister
from resources.user_info import UserInfo
from security import authenticate, identity
from flask_restful import Api
from flask_jwt import JWT


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.secret_key = "jose"
    api = Api(app)

    JWT(app, authenticate, identity)  # /auth

    api.add_resource(Store, "/store/<string:name>")
    api.add_resource(StoreList, "/stores")
    api.add_resource(Item, "/item/<string:name>")
    api.add_resource(ItemList, "/items")
    api.add_resource(UserRegister, "/register")
    api.add_resource(Balance, "/balance/<int:uuid>")
    api.add_resource(Pay, "/pay/<int:uuid>")
    api.add_resource(UserInfo, "/user_info/<int:uuid>")
    return app


if __name__ == "__main__":
    app = create_app()
    from db import db

    db.init_app(app)

    @app.before_first_request
    def create_tables():
        db.create_all()

    app.run()
