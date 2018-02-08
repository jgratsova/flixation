import pymongo


class Database(object):
    # static property shared among all objects of the class
    URI = "mongodb://mongo:27017"
    DATABASE = None
    USERNAME = 'myusername'
    PASSWORD = 'mypassword'

    @staticmethod # allows no self in method
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['movies']
        Database.DATABASE.authenticate(Database.USERNAME,Database.PASSWORD)


    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)


    @staticmethod
    def find(collection):
        return Database.DATABASE[collection].find()

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)
