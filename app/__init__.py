from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os 
from flask_login import LoginManager
from flask_migrate import Migrate

app = Flask(__name__)
# config for forms 

# this key should not be in souce code for production
app.config['SECRET_KEY'] = 'secret321'

# config for db
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

migrate = Migrate(app, db)


#config for login manager

login = LoginManager(app)
login.login_view = "login"

from app import routes