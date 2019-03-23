from flask_pymongo import PyMongo

mongo = None

def init_app(app):
    global mongo
    mongo = PyMongo(app)