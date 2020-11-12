"""Controller to route user functionality"""
from flask import jsonify, Response
from models.user_model import User


def get_users():
    """Gets all users"""
    return_value = jsonify({'users': User.get_all_users()})
    return return_value


def get_by_username(username):
    """Gets a user by username"""
    response = Response(str(User.get_user(username)), 200, mimetype="application/json")
    return response
