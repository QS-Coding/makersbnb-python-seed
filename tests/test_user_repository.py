from lib.repositories.user_repository import *
from lib.models.user import *

def test_get_all_users(db_connection):
    db_connection.seed('seeds/makersbnb_db.sql')
    repository = UserRepository(db_connection)
    users = repository.all()
    assert users[0].id == 1
    assert users[0].email == 'marco@gmail.com'

def test_create_user(db_connection):
    db_connection.seed('seeds/makersbnb_db.sql')
    repository = UserRepository(db_connection)
    repository.create(User(None, 'test@email.com', 'Will Test', 'password'))
    users = repository.all()
    assert users[1].id == 2
    assert users[1].email == 'test@email.com'
    assert users[1].name == 'Will Test'

def test_login(db_connection):
    db_connection.seed('seeds/makersbnb_db.sql')
    repository = UserRepository(db_connection)
    repository.create(User(None, 'test@email.com', 'Will Test', 'password'))
    assert repository.login('test@email.com', 'password') == User(2, 'test@email.com', 'Will Test', None)
    assert repository.login('test@email.com', 'pass') == False
    assert repository.login('test@email.co.uk', 'password') == False

def test_find_user_by_email(db_connection):
    db_connection.seed('seeds/makersbnb_db.sql')
    repository = UserRepository(db_connection)
    repository.create(User(None, 'test@email.com', 'Will Test', 'password'))
    assert repository.find_by_email('test@email.com') == User(2, 'test@email.com', 'Will Test', None)
    assert repository.find_by_email('test@emaasdasil.com') == False

def test_find_user_by_id(db_connection):
    db_connection.seed('seeds/makersbnb_db.sql')
    repository = UserRepository(db_connection)
    repository.create(User(None, 'test@email.com', 'Will Test', 'password'))
    assert repository.find_by_id(2) == User(2, 'test@email.com', 'Will Test', None)
    assert repository.find_by_id(3) == False