from lib.models.my_booking import *
from lib.repositories.my_booking_repo import *
from lib.repositories.booking_repository import *
from lib.models.user import *
from lib.models.booking import *
from lib. repositories.user_repository import *
def test_all_my_bookings(db_connection):
    db_connection.seed('seeds/makersbnb_db.sql')
    mybookingrepo = MyBookingRepo(db_connection)
    booking_repo = BookingRepository(db_connection)
    user_repo = UserRepository(db_connection)
    user_repo.create(User(None, 'test@email.com', 'Will Test', 'password'))
    booking_repo.create(Booking(None, 1, 2, date(2024, 9, 1), date(2024, 9, 4), False, 300.0, date(2024, 7, 1)))

    assert mybookingrepo.all_my_bookings(2) == [
        MyBooking('Studio in London', 1, 'Will Test', 2, False, 300.0, date(2024, 9, 1), date(2024, 9, 4), date(2024, 7, 1))
    ]

def test_all_my_property_bookings(db_connection):
    db_connection.seed('seeds/makersbnb_db.sql')
    mybookingrepo = MyBookingRepo(db_connection)
    booking_repo = BookingRepository(db_connection)
    user_repo = UserRepository(db_connection)
    user_repo.create(User(None, 'test@email.com', 'Will Test', 'password'))
    booking_repo.create(Booking(None, 1, 2, date(2024, 9, 1), date(2024, 9, 4), False, 300.0, date(2024, 7, 1)))

    assert mybookingrepo.all_my_property_bookings(1) == [
        MyBooking('Studio in London', 1, 'Marco Polo', 1, False, 360, date(2024, 7, 5), date(2024, 7, 11), date(2024, 7, 1)),
        MyBooking('Studio in London', 1, 'Will Test', 2, False, 300.0, date(2024, 9, 1), date(2024, 9, 4), date(2024, 7, 1))
    ]

    