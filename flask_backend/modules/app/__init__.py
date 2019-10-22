''' flask app with mongo '''
import os
import json
import datetime
from bson.objectid import ObjectId
from flask import Flask
from pymongo import MongoClient
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from flask_cors import CORS


class JSONEncoder(json.JSONEncoder):
    ''' extend json-encoder class'''

    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        if isinstance(o, set):
            return list(o)
        if isinstance(o, datetime.datetime):
            return str(o)
        return json.JSONEncoder.default(self, o)


# create the flask object
app = Flask(__name__)
app.config['MONGOURL'] = os.environ.get('MONGOURL')
app.config['MONGO_USERNAME'] = os.environ.get('MONGO_USERNAME')
app.config['MONGO_PASSWORD'] = os.environ.get('MONGO_PASSWORD')
app.config['JWT_SECRET_KEY'] = os.environ.get('SECRET')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=1)

# Enable cross origin CORS
cors = CORS(app, resources={r"/*": {"origins": "*"}})

# Create a connection to CosmosDB
client = MongoClient(app.config['MONGOURL'])
db = client.test    #Select the database
db.authenticate(name=app.config['MONGO_USERNAME'],password=app.config['MONGO_PASSWORD'])
flask_bcrypt = Bcrypt(app)
jwt =JWTManager(app)
app.json_encoder = JSONEncoder


from app.controllers import *  # pylint: disable=W0401,C0413