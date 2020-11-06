"""Entry point for our API"""
from flask import Flask, Response

app = Flask(__name__)


@app.route('/')
def welcome():
    """Welcome method for API"""
    response_text = '{ "message": "Hello, welcome to the flask api" }'
    response = Response(response_text, 200, mimetype='application/json')
    return response


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
