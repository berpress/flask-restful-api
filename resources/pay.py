from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from models.balance import BalanceModel
from models.item import ItemModel
from models.user import UserModel


class Pay(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "itemId", type=int, required=True, help="Every item needs a store_id."
    )

    @jwt_required()
    def post(self, uuid):
        data = Pay.parser.parse_args()
        user = UserModel.find_by_id(uuid)
        item = ItemModel.find_by_id(data["itemId"])
        balance = BalanceModel.find_by_id(uuid)
        if not user:
            return {"message": "User not found"}, 404
        if not item:
            return {"message": "Item not found"}, 404
        new_balance = balance.balance - item.price
        if new_balance < 0:
            return {
                "message": f"Not enough money. Your balance is {balance}, "
                f"item cost {item.price}"
            }, 400
        else:
            balance.balance = balance.balance - item.price
        try:
            balance.save_to_db()
        except:
            return {"message": "An error occurred buy item"}, 500
        return {
            "message": "Payment was successful",
            "balance": balance.balance,
            "name": item.name,
            "price": item.price,
        }
