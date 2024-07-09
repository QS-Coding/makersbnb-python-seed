import os

from flask import Flask, request, render_template, redirect, jsonify
from lib.database_connection import get_flask_database_connection
from lib.models.property import Property 
import json
from lib.repositories.property_repository import PropertyRepository


app = Flask(__name__)

@app.route('/index', methods=['GET'])
def get_index():
    return render_template('index.html')


# GET /properties
# to see a list of all properties
@app.route("/properties", methods=['GET'])
def get_all_properties():
    connection = get_flask_database_connection(app)
    repository = PropertyRepository(connection)
    properties = repository.all()
    return render_template("list_all_properties.html", properties=properties)


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.

# @app.route('/p_list', methods=['GET'])
# def property_list():
#     property = json.loads(request.args.get('property'))
#     return render_template('property_list.html', property=property)

@app.route('/property/<int:property_id>', methods=['GET'])
def property_detail(property_id):
    property = json.loads(request.args.get('property'))
    users = json.loads(request.args.get('users'))

    # Find the property by ID
    property = next((space for space in property if space['id'] == property_id), None)
    if property:
        # Find the user by ID
        user = next((user for user in users if user['id'] == property['user_id']), None)
        return render_template('property_detail.html', property=property, user=user)
    else:
        return "Property not found", 404

# GET /properties/new
# Returns a form to create a new property
@app.route('/properties/new', methods=['GET'])
def new_property():
    return render_template('new_property.html') 

# POST /properties
# creates a new property 
@app.route('/properties', methods=['POST'])
def create_property():
    connection = get_flask_database_connection(app)
    repository = PropertyRepository(connection)
    property = Property(None, request.form['name'], request.form['price'], request.form['description'], request.form['available_from'],request.form['available_to'], request.form['owner_id'])
    if not property.is_valid():
        return render_template('properties/new_property.html', 
            property=property, errors=property.generate_errors()), 400 
    property = repository.create(property)
    return redirect(f"/properties/{property.id}")  


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True, port=5001)
