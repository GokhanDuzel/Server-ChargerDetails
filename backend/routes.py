from . import app
import os
import json
import requests
from flask import jsonify, request, make_response, abort, url_for  # noqa; F401

OPEN_CHARGE_MAP_API_URL = 'https://api.openchargemap.io/v3/poi'
API_KEY = '6e929e02-2607-4516-836f-b821114694b1'

######################################################################
# RETURN HEALTH OF THE APP
######################################################################
@app.route("/health")
def health():
    return jsonify(dict(status="OK")), 200

######################################################################
# RETURN FIRST 10 CHARGING STATIONS 
######################################################################
@app.route('/charging-stations', methods=['GET'])
def get_charging_stations():
    params = {
        'key': API_KEY,
        'maxresults': 10,
        'id': id
    }

    try:
        # Make an HTTP GET request to the Open Charge Map API
        response = requests.get(OPEN_CHARGE_MAP_API_URL, params=params)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response data
            data = response.json()
            return jsonify(data)  # Return the API response as JSON

        # If the request was not successful, handle the error
        else:
            return jsonify({'error': 'API request failed'}), response.status_code

    except requests.exceptions.RequestException as e:
        return jsonify({'error': 'API request error'}), 500
    
######################################################################
# RETURN CHARGING STATION DETAILS BY ID 
######################################################################
@app.route('/charging-station/<int:id>', methods=['GET'])
def get_charging_station(id):
    params = {
        'key': API_KEY,
        'id': id
    }
    try:
        # Make an HTTP GET request to the Open Charge Map API
        response = requests.get(OPEN_CHARGE_MAP_API_URL, params=params)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response data
            data = response.json()

            # Access "UsageTypeID"
            usage_type_id = data[0]['AddressInfo']
            return jsonify({'UsageTypeID': usage_type_id})
            # If 'UsageTypeID' doesn't exist, handle the error
        else:
            return jsonify({'error': 'API request failed'}), response.status_code

    except requests.exceptions.RequestException as e:
        return jsonify({'error': 'API request error'}), 500