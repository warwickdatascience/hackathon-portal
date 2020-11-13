from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_login import LoginManager
import pymysql
import datetime
from os.path import join, dirname, realpath

# Globally accessible libraries
db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")

    # initilise plugins
    db.init_app(app)
    # jwt.init_app(app)
    login_manager = LoginManager()
    login_manager.login_view = 'auth_bp.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    with app.app_context():
        # import parts of our application
        from . import auth, submission, finished

        app.register_blueprint(auth.auth_bp)
        app.register_blueprint(submission.submission_bp)
        app.register_blueprint(finished.finished_bp)

        return app
