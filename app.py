import os
from flask import Flask, request, render_template,  jsonify
from lib.database_connection import get_flask_database_connection
import json

app = Flask(__name__)

@app.route('/index', methods=['GET'])
def get_index():
    return render_template('index.html')

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
