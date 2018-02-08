import uuid

from common.database import Database
import datetime


class Movie(object):

    def __init__(self, title, description, file, _id=None):
        self.title = title
        self.description = description
        self.file = file
        self._id = uuid.uuid4().hex if id is None else id

    @classmethod
    def from_mongo(cls, file):
        movie_data = Database.find_one(collection='movies', query={'file': file})
        return movie_data

    @staticmethod
    def from_all():
        return [movie for movie in Database.find(collection='movies')]
