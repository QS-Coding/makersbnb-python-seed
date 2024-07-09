import os
import json
from flask import Flask, request, render_template, redirect, jsonify
from lib.database_connection import get_flask_database_connection

from lib.repositories.user_repository import UserRepository

from lib.models.property import Property 

from lib.repositories.property_repository import PropertyRepository

app = Flask(__name__)

# Route for the homepage
@app.route('/', methods=['GET'])
def get_index():
    """
    Route for the homepage.
    :return: Renders the index.html template.
    """
    return render_template('index.html')

# Route for fetching all properties from the database
@app.route("/properties", methods=['GET'])
def get_all_properties():
    """
    Route for fetching all properties from the database.
    :return: Renders the list_all_properties.html template with the list of properties.
    """
    connection = get_flask_database_connection(app)
    repository = PropertyRepository(connection)
    properties = repository.all()
    return render_template("list_all_properties.html", properties=properties)

# Route for fetching a specific property detail
@app.route('/property/<int:property_id>', methods=['GET'])
def property_detail(property_id):
    """
    Route for the property detail page.
    :param property_id: ID of the property to display.
    :return: Renders the property_detail.html template with the property details and user information.
    """
    connection = get_flask_database_connection(app)
    property_repository = PropertyRepository(connection)
    user_repository = UserRepository(connection)

    # Find the property by ID
    property = property_repository.find(property_id)
    if property:
        # Find the user by ID
        user = user_repository.find_by_id(property.owner_id)
        return render_template('property_detail.html', property=property, user=user)
    else:
        return "Property not found", 404


# List properties owned by a specific user (owner)
@app.route("/properties/owner/<int:owner_id>", methods = ['GET'])
def get_properties_by_owner(owner_id):
    connection = get_flask_database_connection(app)
    repository = PropertyRepository(connection)
    properties = repository.find_by_owner_id(owner_id)
    if properties:
        return render_template('properties_by_owner.html', properties = properties)
    else:
        return "Can't find properties for this owner", 404


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True, port=5001)

