from playwright.sync_api import Page, expect
from lib.repositories.booking_repository import BookingRepository
from lib.models.booking import Booking
from datetime import date

"""
PLAYWRIGHT CLIENT
E2E Test. 
Checking creation of a new booking request
Scenario:
1. Create a new user - "magelan@gmail.com",password = password!1
2. User magelan@gmail.com books a property with id=1 and dates 2024-07-15 to 2024-07-20
3. New booking request appears in database
"""
def test_new_booking(test_web_address, page, db_connection):
    db_connection.seed('seeds/makersbnb_db.sql')
    page.goto(f'http://{test_web_address}/signup')
    page.fill("input[name='name']","Magelan")
    page.fill("input[name='email']","magelan@gmail.com")
    page.fill("input[name='pass']","password!1")
    page.fill("input[name='confpass']","password!1")
    page.click("text='Submit'")
    page.goto(f'http://{test_web_address}/login')
    page.fill("input[name='email']","magelan@gmail.com")
    page.fill("input[name='password']","password!1")
    page.click("text='Login'")
    page.goto(f'http://{test_web_address}/property/1')
    page.fill("input[id='startDate']","12/07/2024")
    page.fill("input[id='endDate']","20/07/2024")
    page.wait_for_timeout(1000)
    page.click("text='Add Property")
    repository = BookingRepository(db_connection)
    assert repository.find_by_id(1) == Booking(1, 1, 2, date(2024, 7, 12), date(2024, 7, 20), False, 480.0, date.now())
