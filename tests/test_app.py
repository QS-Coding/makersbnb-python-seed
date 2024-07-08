from playwright.sync_api import Page, expect

# Tests for your routes go here

# """
# When we call GET /properties we get a list of all properties
# expect response 200 OK 
# """
def test_get_all_properties(db_connection, web_client):
    db_connection.seed("seeds/makersbnb_db.sql")
    response = web_client.get('/properties')
    assert response.status_code == 200 
    assert response.data.decode('utf-8') == '' \
        "Property('Studio in London','Great studio to rent in the heart of London',60.0,'2024-07-01','2024-12-31',1)" 




"""
We can render the index page
"""


def test_get_index(page, test_web_address):
    # We load a virtual browser and navigate to the /index page
    page.goto(f"http://{test_web_address}/index")

    # We look at the <p> tag
    p_tag = page.locator("p")

    # We assert that it has the text "This is the homepage."
    expect(p_tag).to_have_text("This is the homepage.")