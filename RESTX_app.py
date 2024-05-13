"""
Copyright (c) 2024 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
"""
from flask import Flask
from flask_restx import Api, Resource, reqparse
from flask_httpauth import HTTPBasicAuth
import csv
from datetime import datetime, timedelta

app = Flask(__name__)
api = Api(app)
auth = HTTPBasicAuth()

# Define user-password pairs
users = {
    "admin": "secret",
    # Add more user-password pairs as needed
}

# Verify password function for basic authentication
@auth.verify_password
def verify_password(username, password):
    if username in users and users[username] == password:
        return username

# Read CSV data into a list of dictionaries
def read_csv_data():
    with open('pxgrid_direct.csv', mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        items = [row for row in csv_reader]
    return items

# Filter items based on the sys_updated_on field being within a specified number of hours
def filter_items_by_date(items, hours=None):
    if hours is not None:
        now = datetime.now()
        cutoff = now - timedelta(hours=hours)
        items = [
            item for item in items if datetime.strptime(item['sys_updated_on'], "%Y-%m-%d %H:%M:%S") >= cutoff
        ]
    return items

# Request parser for the /endpoints endpoint
parser = reqparse.RequestParser()
parser.add_argument('limit', type=int, required=False, help='Number of items to return.')
parser.add_argument('hours', type=int, required=False, help='Time frame in hours to filter updated items.')

# /endpoints endpoint to get all items or the latest items based on optional limit and hours parameters
@api.route('/endpoints')
class Endpoints(Resource):
    @auth.login_required
    @api.expect(parser, validate=True)
    def get(self):
        args = parser.parse_args()
        limit = args.get('limit')
        hours = args.get('hours')
        items = read_csv_data()
        filtered_items = filter_items_by_date(items, hours=hours)

        if limit is not None:
            filtered_items = filtered_items[:limit]

        return {"result": filtered_items}

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
