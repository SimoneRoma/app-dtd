import mysql.connector
import os

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

user = os.environ['USER']
password = os.environ['PASS']
host = os.environ['HOST']

conn_string = "mysql+mysqlconnector://" + user + ":" + password + "@" + host + ":3306/app"
app.config['SQLALCHEMY_DATABASE_URI'] = conn_string
db = SQLAlchemy(app)

class Item(db.Model):
    item_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    date = db.Column(db.String(100))
    description = db.Column(db.String(250))

    def init_post(self, name, description):
        self.name = name
        self.description = description

    def __init__(self, name, description, date=None):
        self.name = name
        self.description = description
        self.date = date

@app.route('/v1/items', methods=['POST'])
def create_item():
    name = request.json.get('name')
    description = request.json.get('description')

    if not name or not description:
        return jsonify({'error': 'Please provide a name and description.'}), 400

    now = datetime.now()

    new_item = Item(name, description, now)
    db.session.add(new_item)
    db.session.commit()

    return jsonify({'message': 'Item created successfully.'}), 201

@app.route('/v1/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = Item.query.get(item_id)

    if not item:
        return jsonify({'error': 'Item not found.'}), 404

    item_data = {
        'id': item.item_id,
        'date': item.date,
        'name': item.name,
        'description': item.description
    }

    return jsonify(item_data), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
