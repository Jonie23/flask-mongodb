
from flask import Flask
from flask_mongoengine import MongoEngine
from application import config
from .config import Config




app = Flask(__name__)
app.config.from_object(Config)


db = MongoEngine(app)
#db.init_app(app)

from application import route





