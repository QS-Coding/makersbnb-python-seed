import os

from flask import Flask, request, render_template, redirect, jsonify
from lib.database_connection import get_flask_database_connection
from lib.models.property import Property 
import json
#from lib.property_repository import PropertyRepository


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

@app.route('/p_list', methods=['GET'])
def property_list():
    property = json.loads(request.args.get('property'))
    return render_template('property_list.html', property=property)

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


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True, port=5001)
