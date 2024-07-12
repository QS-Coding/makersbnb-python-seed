from playwright.sync_api import Page, expect
from lib.models.user import User
from lib.repositories.user_repository import UserRepository

"""
PLAYWRIGHT CLIENT
Checking creation of a new user via registration form
Scenario:
1. Create a new user - "magelan@gmail.com",password = password!1
2. New user appears in database
"""
def test_new_booking(test_web_address, page, db_connection):
    db_connection.seed('seeds/makersbnb_db.sql')
    page.goto(f'http://{test_web_address}/signup')
    page.fill("input[name='name']","Magelan")
    page.fill("input[name='email']","magelan@gmail.com")
    page.fill("input[name='pass']","password!1")
    page.fill("input[name='confpass']","password!1")
    page.click("text='Submit'")
    repository = UserRepository(db_connection)
    assert repository.find_by_id(2) == User(2,'magelan@gmail.com','Magelan',None)

