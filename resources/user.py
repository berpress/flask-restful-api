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
        if data["username"] is None or data["password"] is None:
            return {
                "message": "Username and password are required fields",
                "code": "BadRequest",
                "status": 400
            }, 400

        find_user = UserModel.find_by_username(data["username"])

        if find_user:
            return {
                "message": f"A user with that username already exists, id is {find_user.id}",
                "code": "BadRequest",
                "status": 400
            }, 400

        user = UserModel(data["username"], data["password"])
        user.save_to_db()
        user_id = user.find_by_username(data["username"]).id

        return {"message": "User created successfully.", "uuid": user_id}, 201
