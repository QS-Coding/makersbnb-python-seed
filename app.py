import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection

app = Flask(__name__)

# List of property spaces
spaces = [
    {"id": 1, "address": "221b Baker Street", "price": 250, "description": "Small one bedroom flat near centre of city", "owner_id": 1},
    {"id": 2, "address": "742 Evergreen Terrace", "price": 300, "description": "Spacious three bedroom house with a large garden", "owner_id": 2},
    {"id": 3, "address": "12 Grimmauld Place", "price": 450, "description": "Charming four bedroom house with historical significance", "owner_id": 3},
    {"id": 4, "address": "4 Privet Drive", "price": 275, "description": "Cozy three bedroom house in a quiet suburban neighborhood", "owner_id": 3},
    {"id": 5, "address": "Bag End, Hobbiton", "price": 320, "description": "Unique two bedroom hobbit-hole with beautiful countryside views", "owner_id": 5},
    {"id": 6, "address": "10 Downing Street", "price": 600, "description": "Prime ministerial residence with state-of-the-art security features", "owner_id": 1},
    {"id": 7, "address": "1007 Mountain Drive", "price": 500, "description": "Luxurious mansion with stunning city views and modern amenities", "owner_id": 4},
    {"id": 8, "address": "42 Wallaby Way, Sydney", "price": 280, "description": "Modern two bedroom apartment with ocean views", "owner_id": 6},
    {"id": 9, "address": "1313 Mockingbird Lane", "price": 350, "description": "Quirky four bedroom house with unique architectural features", "owner_id": 7},
    {"id": 10, "address": "1600 Pennsylvania Avenue NW", "price": 700, "description": "Historic and grand presidential residence with extensive grounds", "owner_id": 2}
]

# List of property owners
owners = [
    {"id": 1, "name": "Martha Hudson", "email": "a.conan@doyle.com", "password": "IamSHerl0ck3d"},
    {"id": 2, "name": "Homer Simpson", "email": "h.simpson@springfield.com", "password": "d0h12345"},
    {"id": 3, "name": "Sirius Black", "email": "s.black@wizardworld.com", "password": "padf00t123"},
    {"id": 4, "name": "Bruce Wayne", "email": "b.wayne@gotham.com", "password": "batc4ve123"},
    {"id": 5, "name": "Bilbo Baggins", "email": "b.baggins@shire.com", "password": "ringbearer123"},
    {"id": 6, "name": "P. Sherman", "email": "p.sherman@sydney.com", "password": "fishfr13ndly"},
    {"id": 7, "name": "Herman Munster", "email": "h.munster@mockingbird.com", "password": "spooky123"}
]

# Route for the homepage
@app.route('/index', methods=['GET'])
def get_index():
    return render_template('index.html')

# Route for the property listing page
@app.route('/p_list', methods=['GET'])
def property_list():
    return render_template('property_list.html', spaces=spaces)

# Route for the property detail page
@app.route('/property/<int:property_id>', methods=['GET'])
def property_detail(property_id):
    # Find the property by ID
    property = next((space for space in spaces if space['id'] == property_id), None)
    if property:
        # Find the owner by ID
        owner = next((owner for owner in owners if owner['id'] == property['owner_id']), None)
        return render_template('property_detail.html', property=property, owner=owner)
    else:
        return "Property not found", 404

if __name__ == '__main__':
    app.run(debug=True, port=5001)
