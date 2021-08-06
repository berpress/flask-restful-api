from db import db


class BalanceModel(db.Model):
    __tablename__ = "balance"

    id = db.Column(db.Integer, primary_key=True)
    balance = db.Column(db.Float(precision=2))

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    user = db.relationship("UserModel")

    def __init__(self, user_id, balance):
        self.user_id = user_id
        self.balance = balance

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
