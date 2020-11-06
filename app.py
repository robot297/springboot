"""Entry point for our API"""
from flask import Response
from config import my_app


def welcome():
    """Welcome method for API"""
    response_text = '{ "message": "Hello, welcome to the flask api" }'
    response = Response(response_text, 200, mimetype='application/json')
    return response


if __name__ == '__main__':
    my_app.run(host='localhost', port=5000, debug=True)
