import os

from flask import Flask, request, render_template, redirect, jsonify, session, abort
import json

from lib.database_connection import get_flask_database_connection

from lib.repositories.user_repository import UserRepository

from lib.models.property import Property 


from lib.repositories.property_repository import PropertyRepository

app = Flask(__name__)
app.config['SECRET_KEY']='1b973299943650f6c7daf012'

# Route for the homepage
@app.route('/', methods=['GET'])
def get_index():
    """
    Route for the homepage.
    :return: Renders the index.html template.
    """
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
        session.pop('user_id')
    return redirect("/index")

# GET /properties
# to see a list of all properties

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

# GET /properties/new
# displays a form to create a new property
@app.route('/properties/new', methods=['GET'])
def new_property():
    if 'user_id' not in session:
        abort(403)
    return render_template('new_property.html') 

# POST /properties
# creates a new property 
@app.route('/properties/created', methods=['POST'])
def create_property():
    if 'user_id' not in session:
        abort(403)
    owner_id = session['user_id']
    connection = get_flask_database_connection(app)
    repository = PropertyRepository(connection)
    property = Property(None, request.form['name'], request.form['description'],request.form['price'], request.form['available_from'],request.form['available_to'], owner_id)
    if not property.is_valid():
        return render_template('properties/new_property.html', 
            property=property, errors=property.generate_errors()), 400 
    property = repository.add(property)
    return redirect(f"/property/{property.id}")  


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

