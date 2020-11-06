"""Controller to route user functionality"""
from flask import jsonify
from models.user_model import User


def get_users():
    """Gets all users"""
    return_value = jsonify({'users': User.get_all_users()})
    return return_value
