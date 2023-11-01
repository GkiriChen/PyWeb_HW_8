import configparser

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from mongoengine import connect

config = configparser.ConfigParser()
config.read('config.ini')

mongo_user = config.get('DB', 'user')
mongodb_pass = config.get('DB', 'pass')
db_name = config.get('DB', 'db_name')
domain = config.get('DB', 'domain')

# uri = f"mongodb+srv://{mongo_user}:{mongodb_pass}@{domain}/?retryWrites=true&w=majority"
# # Create a new client and connect to the server
# client = MongoClient(uri, server_api=ServerApi('1'))

# db = client.db_name

connect(host=f"mongodb+srv://{mongo_user}:{mongodb_pass}@{domain}{db_name}", ssl=True)
