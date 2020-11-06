"""DB config information"""
from flask_sqlalchemy import SQLAlchemy
from config import my_app

db = SQLAlchemy(my_app.app)
