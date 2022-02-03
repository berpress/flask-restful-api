from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from resources.balance import Balance
from resources.pay import Pay
from resources.user_info import UserInfo
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList, WelcomeList
from resources.store import Store, StoreList
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True
app.secret_key = "jose"
api = Api(app)

jwt = JWT(app, authenticate, identity)  # /auth

api.add_resource(Store, "/store/<string:name>")
api.add_resource(StoreList, "/stores")
api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")
api.add_resource(UserRegister, "/register")
api.add_resource(Balance, "/balance/<int:uuid>")
api.add_resource(Pay, "/pay/<int:uuid>")
api.add_resource(UserInfo, "/user_info/<int:uuid>")
api.add_resource(WelcomeList, "/")


if __name__ == "__main__":
    from db import db

    db.init_app(app)

    if app.config["DEBUG"]:

        @app.before_first_request
        def create_tables():
            db.create_all()

    app.run(port=5000)
