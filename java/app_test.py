"""Test suite for the main.py file."""
import json
import connexion
import pytest

flask_app = connexion.FlaskApp(__name__)
flask_app.add_api('../swagger/swagger.yml')


@pytest.fixture(scope='module')
def client():
    """Defines the client we're testing against"""
    with flask_app.app.test_client() as _c:
        yield _c


def helper(json_info):
    """Helps convert and parse responses"""
    for info in json_info:
        first_row = info.decode("utf-8")
        return str(json.loads(first_row))


def test_tc0001_welcome(client):
    """Tests API welcome message"""
    td_message = "{'message': 'Hello, welcome to the flask api'}"
    client_response = client.get('/')
    json_info = helper(client_response.response)
    assert client_response.status_code == 200
    if td_message != json_info:
        print(f'FAIL: Not able to find td {td_message}')
        print(f'Actual Response: {json_info}')
        assert False
