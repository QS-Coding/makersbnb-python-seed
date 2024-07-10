from playwright.sync_api import Page, expect

"""
GET /properties/owner/1
Test non-authenticated request to /properties/owner/1
Expected status code 403
"""
def test_get_properties_by_owner_nonauth(web_client):
    response = web_client.get("/properties/owner/1")
    assert response.status_code == 403

"""
GET /properties/owner/1
Test authenticated request to /properties/owner/1
Expected status code 200 
"""

def test_get_properties_auth(web_client):
    web_client.get("/fake_login")
    response = web_client.get("/properties/owner/1")
    assert response.status_code == 200
    web_client.get("/fake_logout")
    response = web_client.get("/properties/owner/1")
    assert response.status_code == 403

"""
PLAYWRIGHT CLIENT
Checking html content on /properties/owner/1
"""
def test_get_properties_by_owner_content(test_web_address, page, db_connection):
    db_connection.seed('seeds/makersbnb_db.sql')
    page.goto(f'http://{test_web_address}/fake_login')
    page.goto(f'http://{test_web_address}/properties/owner/1')
    a_href=page.locator('a.property-name').first
    expect(a_href).to_have_text("Studio in London")
    page.goto(f'http://{test_web_address}/fake_logout')