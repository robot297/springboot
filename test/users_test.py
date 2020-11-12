"""Contains all user model tests"""
import json
import os
import connexion
import pytest

from config import my_app
from db_config import db

flask_app = connexion.FlaskApp(__name__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(my_app.root_path, 'database/test.db')
flask_app.app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
flask_app.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(flask_app.app)
flask_app.add_api('../swagger/swagger.yml')


@pytest.fixture(scope='module')
def client():
    with flask_app.app.test_client() as c:
        yield c


def helper(json_info):
    """Helper for parsing json"""
    for info in json_info:
        first_row = info.decode("utf-8")
        return str(json.loads(first_row))


def test_tc0001_get(client):
    """Test to check if a single user can be retrieved from the db."""
    td_user = 'thor'
    response = client.get('/users/v1')
    json_info = helper(response.response)
    assert response.status_code == 200
    if td_user not in json_info:
        print(f"FAIL: Not able to find {td_user}")
        print(f"Actual response: {json_info}")
        assert False
