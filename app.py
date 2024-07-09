import os

from flask import Flask, request, render_template, redirect, jsonify, session, abort
from lib.database_connection import get_flask_database_connection
from lib.models.property import Property 
from lib.repositories.property_repository import PropertyRepository
from lib.repositories.user_repository import UserRepository

import json
#from lib.property_repository import PropertyRepository


app = Flask(__name__)
app.config['SECRET_KEY']='1b973299943650f6c7daf012'

@app.route('/index', methods=['GET'])
def get_index():
    return render_template('index.html')


# App fake login endpoint. To be replaced by a real one later.

@app.route("/fake_login",methods = ['GET'])
def fake_login():
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)
    user = repository.login('marco@gmail.com','mypssword') #To be replaced by values from html form.
    if user:
        session['logged_in']=True
        session['email']=user.email 
        session['user_id']=user.id 
        return f"You are logged in as: {session['email']} with id: {user.id}"
    else:
        error = "User email or password is incorrect."
        return error 

# App fake logout endpoint. To be replaced by a real one later.
@app.route("/fake_logout", methods = ['GET'])
def fake_logout():
    if 'logged_in' in session:
        session.pop('logged_in')
    return redirect("/index")

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

# List properties owned by a specific user (owner)
@app.route("/properties/owner/<int:owner_id>", methods = ['GET'])
def get_properties_by_owner(owner_id):
    if 'logged_in' not in session:
        abort(403)
    connection = get_flask_database_connection(app)
    repository = PropertyRepository(connection)
    properties = repository.find_by_owner_id(owner_id)
    if properties:
        if owner_id==session['user_id']:
            return render_template('properties_by_owner.html', properties = properties)
        else:
            abort(403)

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
