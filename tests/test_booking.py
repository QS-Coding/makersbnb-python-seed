from lib.models.booking import *
from datetime import datetime

def test_booking_init():

    booking = Booking(1, 1, datetime(2024, 1, 1), datetime(2024, 1, 3), True, 455.50, datetime(2024, 1, 1))

    assert booking.id == 1
    assert booking.property_id == 1
    assert booking.requested_from == datetime(2024, 1, 1)
    assert booking.requested_to == datetime(2024, 1, 3)
    assert booking.is_confirmed == True

    assert booking.total_price == 455.50
    assert booking.created_at == datetime(2024, 1, 1)

def test_str_repr():
    booking = Booking(1, 1, datetime(2024, 1, 1), datetime(2024, 1, 3), True, 455.50, datetime(2024, 1, 1))
    assert str(booking) == 'Booking(1, 1, 2024-01-01 00:00:00, 2024-01-03 00:00:00, True, 455.50, 2024-01-01 00:00:00)'

def test_eq():
    booking = Booking(1, 1, datetime(2024, 1, 1), datetime(2024, 1, 3), True, 455.50, datetime(2024, 1, 1))
    assert booking == Booking(1, 1, datetime(2024, 1, 1), datetime(2024, 1, 3), True, 455.50, datetime(2024, 1, 1))
