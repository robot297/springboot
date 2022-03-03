"""Basic API functions"""
import logging
from flask import Response
from flask_caching import Cache
from config import my_app
from db_config import db
from models.user_model import User


logger = logging.getLogger(__name__)
cache = Cache(my_app.app)

@my_app.route('/dbsetup')
def create_db():
    """Creates database with some data populated."""
    db.drop_all()
    db.create_all()
    User.add_user_td()
    response_text = '{ "message": "Database created" }'
    response = Response(response_text, 200, mimetype='application/json')
    return response


@cache.cached(timeout=60)
def welcome():
    """Welcome method for API"""
    response_text = '{ "message": "Hello, welcome to the flask api" }'
    response = Response(response_text, 200, mimetype='application/json')
    logger.info('Hellloooooo')
    return response


def health():
    """Health check for the API"""
    response_text = '{ "status": "OK" }'
    response = Response(response_text, 200, mimetype='application/json')
    return response
