from lib.models.my_booking import *
from datetime import date

def test_init_my_booking():
    mybooking = MyBooking('Studio in London', 1, 'Marco Polo', 1, False, 360, date(2024, 7, 5), date(2024, 7, 11))
    assert mybooking.property_name == 'Studio in London'
    assert mybooking.owner_id == 1
    assert mybooking.requested_by == 'Marco Polo'