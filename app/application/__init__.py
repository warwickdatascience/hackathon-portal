from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
import pymysql
import datetime

# Globally accessible libraries
db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    # initalise application
    UPLOAD_FOLDER = '/static/'
    ALLOWED_EXTENSIONS = {'csv', 'ipynb'}

    app = Flask(__name__, instance_relative_config=False)
    app.config['SECRET_KEY']  = 'sFsdaffgWE43124frey'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.config.from_object("config.Config")

    # initilise plugins
    db.init_app(app)
    jwt.init_app(app)

    
    with app.app_context():
        # import parts of our application
        from . import token, submission

        app.register_blueprint(token.token_bp)
        app.register_blueprint(submission.submission_bp)

        return app
