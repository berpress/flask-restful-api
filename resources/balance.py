from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from models.balance import BalanceModel
from models.user import UserModel


class Balance(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "balance", type=float, required=True, help="This field cannot be left blank!"
    )

    @jwt_required()
    def get(self, uuid):
        user_balance = BalanceModel.find_by_id(uuid)
        if user_balance:
            return {"message": f"User balance is {user_balance.balance}"}, 200
        return {"message": "Balance not found. Add money for user."}, 404

    @jwt_required()
    def post(self, uuid):
        user = UserModel.find_by_id(uuid)
        data = Balance.parser.parse_args()
        balance = BalanceModel.find_by_id(uuid)
        if not user:
            return {"message": "User not found."}, 404
        if balance:
            balance.balance = data["balance"] + balance.balance
        else:
            balance = BalanceModel(uuid, **data)

        try:
            balance.save_to_db()
        except:
            return {"message": "An error occurred add balance."}, 500
        return {
            "message": f"User balance has been updated. New balance is "
            f"{balance.balance}"
        }, 201
