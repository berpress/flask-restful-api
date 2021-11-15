from db import db


class ItemModel(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))
    image = db.Column(db.String(80))
    description = db.Column(db.String(240))

    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"))
    store = db.relationship("StoreModel")

    def __init__(self, name, price, store_id, description, image):
        self.name = name
        self.price = price
        self.store_id = store_id
        self.description = description
        self.image = image

    def json(self, uuid):
        return {
            "name": self.name,
            "price": self.price,
            "itemID": uuid,
            "description": self.description,
            "image": self.image,
        }

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
