from playwright.sync_api import Page, expect
import pytest
from app import app
import json

# List of property property
property = [
    {"id": 1, "address": "221b Baker Street", "price": 250, "description": "Small one bedroom flat near centre of city", "user_id": 1},
    {"id": 2, "address": "742 Evergreen Terrace", "price": 300, "description": "Spacious three bedroom house with a large garden", "user_id": 2},
    {"id": 3, "address": "12 Grimmauld Place", "price": 450, "description": "Charming four bedroom house with historical significance", "user_id": 3},
    {"id": 4, "address": "4 Privet Drive", "price": 275, "description": "Cozy three bedroom house in a quiet suburban neighborhood", "user_id": 3},
    {"id": 5, "address": "Bag End, Hobbiton", "price": 320, "description": "Unique two bedroom hobbit-hole with beautiful countryside views", "user_id": 5},
    {"id": 6, "address": "10 Downing Street", "price": 600, "description": "Prime ministerial residence with state-of-the-art security features", "user_id": 1},
    {"id": 7, "address": "1007 Mountain Drive", "price": 500, "description": "Luxurious mansion with stunning city views and modern amenities", "user_id": 4},
    {"id": 8, "address": "42 Wallaby Way, Sydney", "price": 280, "description": "Modern two bedroom apartment with ocean views", "user_id": 6},
    {"id": 9, "address": "1313 Mockingbird Lane", "price": 350, "description": "Quirky four bedroom house with unique architectural features", "user_id": 7},
    {"id": 10, "address": "1600 Pennsylvania Avenue NW", "price": 700, "description": "Historic and grand presidential residence with extensive grounds", "user_id": 2}
]

# List of property users
users = [
    {"id": 1, "name": "Martha Hudson", "email": "a.conan@doyle.com", "password": "IamSHerl0ck3d"},
    {"id": 2, "name": "Homer Simpson", "email": "h.simpson@springfield.com", "password": "d0h12345"},
    {"id": 3, "name": "Sirius Black", "email": "s.black@wizardworld.com", "password": "padf00t123"},
    {"id": 4, "name": "Bruce Wayne", "email": "b.wayne@gotham.com", "password": "batc4ve123"},
    {"id": 5, "name": "Bilbo Baggins", "email": "b.baggins@shire.com", "password": "ringbearer123"},
    {"id": 6, "name": "P. Sherman", "email": "p.sherman@sydney.com", "password": "fishfr13ndly"},
    {"id": 7, "name": "Herman Munster", "email": "h.munster@mockingbird.com", "password": "spooky123"}
]

@pytest.fixture
def client():


    # We assert that it has the text "This is the homepage."
    expect(p_tag).to_have_text("This is the homepage.")


"""
When we call GET /properties we get a list of all properties
expect response 200 OK 
"""
def test_get_all_properties(db_connection, web_client):
    db_connection.seed("seeds/makersbnb_db.sql")
    response = web_client.get('/properties')
    assert response.status_code == 200 
    assert response.data.decode('utf-8') == '' \
        "Property('Studio in London','Great studio to rent in the heart of London',60.0,'2024-07-01','2024-12-31',1)" 

    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_route(client):

    response = client.get('/index')
    assert response.status_code == 200
    assert b'This is the homepage.' in response.data

def test_property_list_route(client):

    response = client.get('/p_list', query_string={'property': json.dumps(property)})
    assert response.status_code == 200
    assert b'Current Listings - Maker\'s Bnb' in response.data
    for space in property:
        assert space['address'].encode() in response.data

def test_property_detail_route(client):

    response = client.get('/property/1', query_string={'property': json.dumps(property), 'users': json.dumps(users)})
    assert response.status_code == 200
    assert b'221b Baker Street' in response.data
    assert b'Martha Hudson' in response.data

    response = client.get('/property/999', query_string={'property': json.dumps(property), 'users': json.dumps(users)})
    assert response.status_code == 404

