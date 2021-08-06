from db import db


class UserInfoModel(db.Model):
    __tablename__ = "users_info"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    street = db.Column(db.String(20))
    city = db.Column(db.String(20))
    home_number = db.Column(db.Integer)
    phone = db.Column(db.String(20))
    email = db.Column(db.String(20))

    def __init__(self, user_id, address, phone, email):
        self.user_id = user_id
        self.street = address.get("street")
        self.city = address.get("city")
        self.home_number = address.get("home_number")
        self.phone = phone
        self.email = email

    def json(self, uuid):
        return {
            "city": self.city,
            "street": self.street,
            "userID": uuid,
            "phone": self.phone,
            "email": self.email,
        }

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(user_id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
