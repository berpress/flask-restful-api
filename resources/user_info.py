from flask_restful import Resource, reqparse

from models.user import UserModel
from models.user_info import UserInfoModel
from flask_jwt import jwt_required


class UserInfo(Resource):
    root_parser = reqparse.RequestParser()
    root_parser.add_argument(
        "address", type=dict, help="This field cannot be left blank!"
    )
    root_parser.add_argument("phone", type=str, help="This field cannot be left blank!")
    root_parser.add_argument("email", type=str, help="This field cannot be left blank!")

    address_parser = reqparse.RequestParser()
    address_parser.add_argument("street", type=dict, location=("address",))
    address_parser.add_argument("city", type=dict, location=("address",))
    address_parser.add_argument("home_number", type=dict, location=("address",))

    @jwt_required()
    def get(self, uuid):
        info = UserInfoModel.find_by_id(uuid)
        if info:
            return info.json(uuid)
        return {"message": "User info not found"}, 404

    @jwt_required()
    def post(self, uuid):
        if not UserModel.find_by_id(uuid):
            return {"message": "User not found"}, 404
        data = UserInfo.root_parser.parse_args()
        info = UserInfoModel.find_by_id(uuid)
        if info:
            return {"message": "User info already exists"}, 400
        info = UserInfoModel(uuid, **data)
        try:
            info.save_to_db()
        except:
            return {"message": "An error occurred inserting user info."}, 500
        return {"message": "User info created successfully."}

    @jwt_required()
    def delete(self, uuid):
        info = UserInfoModel.find_by_id(uuid)
        if info:
            info.delete_from_db()
            return {"message": "User info deleted."}, 200
        return {"message": "User info not found."}, 404

    @jwt_required()
    def put(self, uuid):
        data = UserInfo.root_parser.parse_args()
        info = UserInfoModel.find_by_id(uuid)
        if info:
            info.street = data["address"]["street"]
            info.city = data["address"]["city"]
            info.home_number = data["address"]["home_number"]
            info.phone = data["phone"]
            info.email = data["email"]
        else:
            return {"message": "User info not found."}, 404
        info.save_to_db()
        return {"message": "User info updated successfully."}
