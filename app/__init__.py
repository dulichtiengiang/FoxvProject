import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

# def create_app(config_file='setting.py'):
def create_app(config_file='setting.py'):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'squite:///db.sqlite'
    db.init_app(app)
    
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
#     # from app import main
# 