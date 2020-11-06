"""Basic API functions"""
from flask import Response


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
