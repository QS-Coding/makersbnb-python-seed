import os
from flask import Flask, request, render_template, redirect, jsonify, session, abort, url_for, send_from_directory, current_app
import json
from datetime import datetime, date
from datetime import datetime, date
from lib.database_connection import get_flask_database_connection
from lib.repositories.user_repository import UserRepository
from lib.models.property import Property
from lib.models.booking import Booking
from lib.models.user import User
from lib.repositories.property_repository import PropertyRepository
from lib.repositories.booking_repository import BookingRepository

app = Flask(__name__)
app.config['SECRET_KEY']='1b973299943650f6c7daf012'

# Route for the sign up page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """
    Route for the homepage.
    :return: Renders the index.html template.
    """
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        pass_1 = request.form['pass']
        pass_2 = request.form['confpass']
        if pass_1 != pass_2:
            error = "The passwords dont match."
            return render_template('sighnup.html', error=error)
        else: 
            connection = get_flask_database_connection(app)
            repository = UserRepository(connection) 
            new_user = User(None, email=email, name=name, password=pass_1)    
            repository.create(new_user)
            return redirect(url_for('login'))
    return render_template('signup.html')


@app.route('/', methods=['GET'])
def dashboard():
    """
    Route for the homepage.
    :return: Renders the index.html template.
    """
    return render_template('Home.html')


# Route for login (temporary, replace with actual logic)
@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Route for login.
    :return: Renders the login.html template on GET, processes login on POST.
    """
    if request.method == 'POST':
        connection = get_flask_database_connection(app)
        repository = UserRepository(connection)
        user = repository.login (request.form['email'],request.form['password'])
        if user:
            session['logged_in']=True
            session['email']=user.email 
            session['user_id']=user.id 
            # return f"You are logged in as: {session['email']} with id: {user.id}"
            return redirect(url_for('dashboard'))
        else:
            error = "User email or password is incorrect."
        return render_template('login.html', error=error)
    return render_template('login.html')    

# Route for logging out
@app.route('/logout')
def logout():
    """
    Route for logging out.
    :return: Redirects to the homepage.
    """
    session.pop('logged_in', None)
    session.pop('email', None)
    session.pop('user_id',None)
    return redirect(url_for('dashboard'))

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


# GET /properties/new
# displays a form to create a new property
@app.route('/properties/new', methods=['GET'])
def new_property():
    if 'user_id' not in session:
        return redirect(url_for('login'))
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
        return redirect(url_for('login'))
    connection = get_flask_database_connection(app)
    repository = PropertyRepository(connection)
    properties = repository.find_by_owner_id(owner_id)
    if properties:
        if owner_id==session['user_id']:
            return render_template('properties_by_owner.html', properties = properties)
        else:
            return f"<h3> Sorry, but you can see detail of your properties only. </h3>"
        
"""
Bookings endpoints section
"""

# Add new booking for the specific property
@app.route("/bookings/new", methods = ['POST'])
def new_booking():
    if 'logged_in' not in session:
        return redirect(url_for('login'))
    property_id = request.form['property_id']
    user_id = session['user_id']
    requested_from = request.form['startDate']
    requested_to = request.form['endDate']
    title = request.form['title']
    price = request.form['price']
    if property_id!="" and user_id!="" and requested_from!="" and requested_to!="" and title!="":
        connection = get_flask_database_connection(app)
        booking_repository = BookingRepository(connection)
        days = datetime.strptime(requested_to, '%Y-%m-%d').date() - datetime.strptime(requested_from, '%Y-%m-%d').date()
        total_price = float(price) * float(days.days)
        booking = Booking(None,property_id=property_id, user_id=user_id, requested_from=requested_from, requested_to=requested_to, is_confirmed=False, total_price=total_price,created_at=datetime.now())
        booking_repository.create(booking)
    else:
        error = "It seems you haven't specified the dates of your booking request."
        return f"<h3>{error}</h3>"
    return redirect(url_for('my_bookings'))

# List booking requests created by me
# FOR KARLA TO SUBSTITUTE WITH HER FUNCTION
@app.route("/bookings/my", methods = ['GET'])
def my_bookings():
    if 'logged_in' not in session:
        return redirect(url_for('login'))
    connection = get_flask_database_connection(app)
    booking_repository = BookingRepository(connection)
    my_requests = booking_repository.all_bookings_of_user(session['user_id'])
    print (f"HERE MY BOOKINGS!!")
    print (f"{my_requests}")
    return render_template("my_bookings.html", my_requests = my_requests)


# Route for adding a booking
# @app.route('/add_booking', methods=['POST'])
# def add_booking():
#     """
#     Route for adding a booking.
#     :return: JSON response indicating success or failure.
#     """
#     data = request.get_json()
#     start_date = data['startDate']
#     end_date = data['endDate']
#     title = data['title']

#     connection = get_flask_database_connection(app)
#     booking_repository = BookingRepository(connection)

#     # Create a new booking object
#     booking = Booking(
#         property_id=1,  # Replace with actual property_id
#         user_id=1,      # Replace with actual user_id
#         requested_from=start_date,
#         requested_to=end_date,
#         is_confirmed=False,
#         total_price=100,  # Replace with actual price calculation
#         created_at=datetime.now()
#     )

#     try:
#         booking_repository.create(booking)
#         return jsonify({'status': 'success'})
#     except Exception as e:
#         print(e)
#         return jsonify({'status': 'failure'}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

