from models.item import ItemModel
from models.store import StoreModel
from models.user import UserModel


def test_new_user():
    """
    Check user model
    """
    user = UserModel("patkennedy79@gmail.com", "FlaskIsAwesome")
    assert user.username == "patkennedy79@gmail.com"
    assert user.password == "FlaskIsAwesome"


def test_new_item():
    """
    Check item model
    """
    item = ItemModel(name="TestItem", price=100.0, store_id=1)
    assert item.store_id == 1
    assert item.price == 100.0
    assert item.name == "TestItem"


def test_new_store():
    """
    Check store model
    """
    store = StoreModel(name="FlaskIsAwesome")
    store.name = "FlaskIsAwesome"


def test_new_user_balance():
    """
    Check user model
    """
    user = UserModel("patkennedy79@gmail.com", "FlaskIsAwesome")
    assert user.username == "patkennedy79@gmail.com"
    assert user.password == "FlaskIsAwesome"
