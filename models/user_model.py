"""Model for users and database methods"""
from db_config import db
import json


class User(db.Model):
    """Model for users"""
    __tablename__ = 'users'
    username = db.Column(db.String(80), primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def json(self):
        """Returns a data dictionary"""
        return {
            'username': self.username,
            'email': self.email
        }

    @staticmethod
    def get_all_users():
        """Gets all users"""
        return [User.json(user) for user in User.query.all()]

    @staticmethod
    def get_user(_username):
        """Gets a single user"""
        query = User.query.filter_by(username=_username).first()
        return query

    @staticmethod
    def add_user(_username, _email):
        """Function adds a user to a db table."""
        new_user = User(username=_username, email=_email)
        db.session.add(new_user)
        db.session.commit()

    @staticmethod
    def add_user_td():
        """Adds test users to the database"""
        User.add_user("darth", "darth.vader@gmail.com")
        User.add_user("superman", "super.man@gmail.com")
        User.add_user("thor", "thor@gmail.com")

    def __repr__(self):
        """Printable representation of our Model"""
        user_object = {
            'username': self.username,
            'email': self.email
        }
        return json.dumps(user_object)
