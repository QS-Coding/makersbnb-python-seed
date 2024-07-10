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

def test_is_valid():
    user = User(1, 'example@email.com', 'First Last', 'password123')
    user2 = User(2, '', 'First Last', 'password123')
    user3 = User(3, 'example@email.com', None, 'password123')
    user4 = User(3, 'example@email.com', 'First Last', None)
    assert user.is_valid() == True
    assert user2.is_valid() == False
    assert user3.is_valid() == False
    assert user4.is_valid() == False

def test_generate_errors():
    user = User(1, '', 'First Last', 'password123')
    user2 = User(2, 'example@email.com', '', None)
    assert user.generate_errors() == 'You need to enter a name'
    assert user2.generate_errors() == 'You need to enter an email, You need to enter a password'

