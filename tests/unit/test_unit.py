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
    Check user model
    """
    user = UserModel("patkennedy79@gmail.com", "FlaskIsAwesome")
    assert user.username == "patkennedy79@gmail.com"
    assert user.password == "FlaskIsAwesome"


def test_new_store():
    """
    Check user model
    """
    user = UserModel("patkennedy79@gmail.com", "FlaskIsAwesome")
    assert user.username == "patkennedy79@gmail.com"
    assert user.password == "FlaskIsAwesome"


def test_new_user_info():
    """
    Check user model
    """
    user = UserModel("patkennedy79@gmail.com", "FlaskIsAwesome")
    assert user.username == "patkennedy79@gmail.com"
    assert user.password == "FlaskIsAwesome"
