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
    spaces = json.loads(request.args.get('spaces'))
    return render_template('property_list.html', spaces=spaces)

@app.route('/property/<int:property_id>', methods=['GET'])
def property_detail(property_id):
    spaces = json.loads(request.args.get('spaces'))
    owners = json.loads(request.args.get('owners'))

    # Find the property by ID
    property = next((space for space in spaces if space['id'] == property_id), None)
    if property:
        # Find the owner by ID
        owner = next((owner for owner in owners if owner['id'] == property['owner_id']), None)
        return render_template('property_detail.html', property=property, owner=owner)
    else:
        return "Property not found", 404

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True, port=5001)
