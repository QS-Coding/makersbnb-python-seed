import os
from flask import Flask, request, render_template, redirect, jsonify, session, abort, url_for
import json
from datetime import datetime
from lib.database_connection import get_flask_database_connection
from lib.repositories.user_repository import UserRepository
from lib.models.property import Property
from lib.models.booking import Booking
from lib.repositories.property_repository import PropertyRepository
from lib.repositories.booking_repository import BookingRepository

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

# Route for login (temporary, replace with actual logic)
@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Route for login.
    :return: Renders the login.html template on GET, processes login on POST.
    """
    if request.method == 'POST':
        # Implement login logic here
        session['logged_in'] = True
        session['username'] = request.form['username']
        return redirect(url_for('get_index'))
    return render_template('login.html')

# Route for logging out
@app.route('/logout')
def logout():
    """
    Route for logging out.
    :return: Redirects to the homepage.
    """
    session.pop('logged_in', None)
    session.pop('username', None)
    return redirect(url_for('get_index'))

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

# Route for adding a booking
@app.route('/add_booking', methods=['POST'])
def add_booking():
    """
    Route for adding a booking.
    :return: JSON response indicating success or failure.
    """
    data = request.get_json()
    start_date = data['startDate']
    end_date = data['endDate']
    title = data['title']

    connection = get_flask_database_connection(app)
    booking_repository = BookingRepository(connection)

    # Create a new booking object
    booking = Booking(
        property_id=1,  # Replace with actual property_id
        user_id=1,      # Replace with actual user_id
        requested_from=start_date,
        requested_to=end_date,
        is_confirmed=False,
        total_price=100,  # Replace with actual price calculation
        created_at=datetime.now()
    )

    try:
        booking_repository.create(booking)
        return jsonify({'status': 'success'})
    except Exception as e:
        print(e)
        return jsonify({'status': 'failure'}), 500


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
