from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "username", type=str, required=True, help="This field cannot be blank."
    )
    parser.add_argument(
        "password", type=str, required=True, help="This field cannot be blank."
    )

    @staticmethod
    def post():
        data = UserRegister.parser.parse_args()

        find_user = UserModel.find_by_username(data["username"])

        if find_user:
            return {
                "message": "A user with that username already exists",
                "uuid": find_user.id,
            }, 400

        user = UserModel(data["username"], data["password"])
        user.save_to_db()
        user_id = user.find_by_username(data["username"]).id

        return {"message": "User created successfully.", "uuid": user_id}, 201
