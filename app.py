"""Entry point for our API"""
from config import my_app


if __name__ == '__main__':
    my_app.run(host='localhost', port=5000, debug=True)
