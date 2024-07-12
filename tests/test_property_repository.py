from lib.repositories.property_repository import *
from lib.models.property import *
from datetime import date

def test_all(db_connection):
    db_connection.seed('seeds/makersbnb_db.sql')
    repository = PropertyRepository(db_connection)
    assert repository.all() == [Property(1, 'Studio in London', 'Great studio to rent in the heart of London', 60.0, date(2024,7, 1), date(2024,12,31), 1)]

def test_create_property(db_connection):
    db_connection.seed('seeds/makersbnb_db.sql')
    repository = PropertyRepository(db_connection)
    assert repository.add(Property(None, 'Villa in Spain', 'Nice villa', 80.0, date(2024,1,1), date(2024, 1, 31), 1)) == Property(2, 'Villa in Spain', 'Nice villa', 80.0, date(2024,1,1), date(2024, 1, 31), 1)
    assert  repository.all() == [
        Property(1, 'Studio in London', 'Great studio to rent in the heart of London', 60.0, date(2024,7, 1), date(2024,12,31), 1),
        Property(2, 'Villa in Spain', 'Nice villa', 80.0, date(2024,1,1), date(2024, 1, 31), 1)
    ]


def test_find(db_connection):
    db_connection.seed('seeds/makersbnb_db.sql')

    repository = PropertyRepository(db_connection)

    repository.add(Property(None, 'Villa in Spain', 'Nice villa', 80.0, date(2024,1,1), date(2024, 1, 31), 1))
    assert repository.find(2) == Property(2, 'Villa in Spain', 'Nice villa', 80.0, date(2024,1,1), date(2024, 1, 31), 1)
    assert repository.find(3) == False

def test_find_by_owner(db_connection):
    db_connection.seed('seeds/makersbnb_db.sql')
    repository = PropertyRepository(db_connection)
    repository.add(Property(None, 'Villa in Spain', 'Nice villa', 80.0, date(2024,1,1), date(2024, 1, 31), 1))
    assert repository.find_by_owner_id(1) == [
        Property(1, 'Studio in London', 'Great studio to rent in the heart of London', 60.0, date(2024,7, 1), date(2024,12,31), 1),
        Property(2, 'Villa in Spain', 'Nice villa', 80.0, date(2024,1,1), date(2024, 1, 31), 1)
    ]