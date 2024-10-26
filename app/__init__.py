import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from extentions import db, login_manager  # Make sure to import the right instances


def create_app():
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object('config.Config')

    # Initialize Extensions
    db.init_app(app)  # Initialize the db instance with the app

    # Initialize Flask Login
    login_manager.init_app(app)
    login_manager.login_view = 'main.login'
    login_manager.login_message_category = 'info'

    # User loader for Flask-Login
    @login_manager.user_loader
    def load_user(user_id):
        from .models import User
        return User.query.get(int(user_id))

    # Create Database tables
    with app.app_context():
        db.create_all()
    
    # Register blueprint
    from .routes import main
    app.register_blueprint(main)

    return app
