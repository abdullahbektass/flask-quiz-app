from flask import Flask
from flask_bcrypt import Bcrypt
from flask_pymongo import PyMongo
from flask_login import LoginManager
import os


mongo = PyMongo()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'main.login'


def create_app():
    app = Flask(__name__)
    app.config['MONGO_URI'] = os.getenv('MONGO_URI')
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    app.config['SESSION_COOKIE_SECURE'] = False 
    app.config['REMEMBER_COOKIE_SECURE'] = False

    mongo.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from .routes import main
    app.register_blueprint(main)

    return app