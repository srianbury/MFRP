from pymongo import MongoClient
import json

mongo_client = None

def init_app(mongo_uri):
    global mongo_client
    mongo = MongoClient(mongo_uri)
   

def example():
    collection = mongo_client['your db name']['your collection name']
    data = collection.find_one({})['column name']
    return json.dumps(data)
