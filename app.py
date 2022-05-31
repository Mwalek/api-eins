import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from flask_cors import CORS

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

db_url = os.environ.get('DATABASE_URL', 'sqlite:///data.db')

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres", "postgresql", 1)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'mwalek'
api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>') # http://127.0.0.1:5000/item/name
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores/')

api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)