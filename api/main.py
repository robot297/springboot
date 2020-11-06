"""Basic API functions"""
from flask import Response
from config import my_app
from db_config import db
from models.user_model import User


@my_app.route('/dbsetup')
def create_db():
    """Creates database with some data populated."""
    db.drop_all()
    db.create_all()
    User.add_user_td()
    response_text = '{ "message": "Database created" }'
    response = Response(response_text, 200, mimetype='application/json')
    return response


def welcome():
    """Welcome method for API"""
    response_text = '{ "message": "Hello, welcome to the flask api" }'
    response = Response(response_text, 200, mimetype='application/json')
    return response


def health():
    """Health check for the API"""
    response_text = '{ "status": "OK" }'
    response = Response(response_text, 200, mimetype='application/json')
    return response
