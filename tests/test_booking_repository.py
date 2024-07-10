from lib.repositories.booking_repository import *
from lib.models.booking import *
from datetime import date

def test_all_unconfirmed_bookings(db_connection):
    db_connection.seed('seeds/makersbnb_db.sql')
    repository = BookingRepository(db_connection)

    unconfirmed_bookings = repository.all_unconfirmed()
    assert unconfirmed_bookings[0] == Booking(1, 1, 1, date(2024, 7, 5), date(2024, 7, 11), False, 360.0, date(2024, 7, 1))

def test_create(db_connection):
    db_connection.seed('seeds/makersbnb_db.sql')
    repository = BookingRepository(db_connection)
    booking = Booking(None, 1, 1, date(2024, 9, 1), date(2024, 9, 4), None, 300.0, date(2024, 7, 9))
    repository.create(booking)
    assert repository.all_unconfirmed()[1] == Booking(2, 1, 1, date(2024, 9, 1), date(2024, 9, 4), False, 300.0, date(2024, 7, 9))

def test_find_by_id(db_connection):
    db_connection.seed('seeds/makersbnb_db.sql')
    repository = BookingRepository(db_connection)
    booking = Booking(None, 1, 1, date(2024, 9, 1), date(2024, 9, 4), None, 300.0, date(2024, 7, 9))
    repository.create(booking)
    assert repository.find_by_id(2) == Booking(2, 1, 1, date(2024, 9, 1), date(2024, 9, 4), False, 300.0, date(2024, 7, 9))

def test_confirm_booking(db_connection):
    db_connection.seed('seeds/makersbnb_db.sql')
    repository = BookingRepository(db_connection)
    repository.create(Booking(None, 1, 1, date(2024, 9, 1), date(2024, 9, 4), None, 300.0, date(2024, 7, 9)))
    repository.confirm_booking(2)
    booking = repository.find_by_id(2)
    assert booking.is_confirmed == True

def test_all_confirmed_bookings(db_connection):
    db_connection.seed('seeds/makersbnb_db.sql')
    repository = BookingRepository(db_connection)
    repository.create(Booking(None, 1, 1, date(2024, 9, 1), date(2024, 9, 4), None, 300.0, date(2024, 7, 9)))
    repository.confirm_booking(2)
    assert repository.all_confirmed()[0] == Booking(2, 1, 1, date(2024, 9, 1), date(2024, 9, 4), True, 300.0, date(2024, 7, 9))

def test_all_bookings_by_user_id(db_connection):
    db_connection.seed('seeds/makersbnb_db.sql')

    repository = BookingRepository(db_connection)
    repository.create(Booking(None, 1, 1, date(2024, 9, 1), date(2024, 9, 4), None, 300.0, date(2024, 7, 9)))
    assert repository.all_bookings_of_user(1) == [
        Booking(1, 1, 1, date(2024, 7, 5), date(2024, 7, 11), False, 360.0, date(2024, 7, 1)),
        Booking(2, 1, 1, date(2024, 9, 1), date(2024, 9, 4), False, 300.0, date(2024, 7, 9))
    ]
def test_all_bookings_by_property_id(db_connection):
    db_connection.seed('seeds/makersbnb_db.sql')

    repository = BookingRepository(db_connection)
    repository.create(Booking(None, 1, 1, date(2024, 9, 1), date(2024, 9, 4), None, 300.0, date(2024, 7, 9)))
    assert repository.all_bookings_of_property(1) == [
        Booking(1, 1, 1, date(2024, 7, 5), date(2024, 7, 11), False, 360.0, date(2024, 7, 1)),
        Booking(2, 1, 1, date(2024, 9, 1), date(2024, 9, 4), False, 300.0, date(2024, 7, 9))
    ]

