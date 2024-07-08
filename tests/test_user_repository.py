from lib.repositories.user_repository import *

def test_get_all_users(db_connection):
    db_connection.seed('seeds/makersbnb_db.sql')