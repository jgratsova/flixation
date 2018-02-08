import datetime
from flask import session

from common.database import Database
import uuid

from models.movie import Movie


class User(object):
    def __init__(self, email, password, _id=None):
        self.email = email
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id

    @classmethod
    def get_by_email(cls, email):
        data = Database.find_one("users", {"email": email})
        if data is not None:
            return cls(**data)

    @classmethod
    def get_by_id(cls, _id):
        data = Database.find_one("users", {"_id": _id})
        if data is not None:
            return cls(**data)

    @staticmethod
    def login_valid(email, password):
        # User.login_valid("test@test.com", "password")
        # validate login details
        user = User.get_by_email(email)
        if user is not None:
            print("valid login")
            return user.password == password

        print("invalid login")
        return False

    @classmethod
    def register(cls, email, password):
        user = User.get_by_email(email)
        if user is None:
            # doesn't exist create
            new_user = cls(email, password)
            new_user.save_to_mongo()
            session['email'] = email
            return True
        else:
            # User exists
            return False

    @staticmethod
    def login(user_email):
        # login_valid been already called
        print(user_email)
        session['email'] = user_email

    @staticmethod
    def logout():
        session['email'] = None

    def get_movies(self):
        return Movie.from_all()

    def json(self):
        return{
            "email": self.email,
            "_id": self._id,
            "password": self.password
        }

    def save_to_mongo(self):
        Database.insert("users", self.json())
