from lib.models.user import *

def test_user_init():
    user = User(1, 'example@email.com', 'First Last', 'password123')
    assert user.id == 1
    assert user.email == 'example@email.com'
    assert user.name == 'First Last'
    assert user.password == 'password123'

def test_user_str_rep():
    user = User(1, 'example@email.com', 'First Last', 'password123')
    assert str(user) == 'User(1, example@email.com, First Last, password123)'

def test_eq():
    user = User(1, 'example@email.com', 'First Last', 'password123')
    assert user == User(1, 'example@email.com', 'First Last', 'password123')