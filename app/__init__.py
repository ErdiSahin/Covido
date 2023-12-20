from flask import Flask, request, redirect, render_template
from flask_login import login_user, logout_user, current_user, login_required
from flask_login import LoginManager

import os



app = Flask(__name__)

app.secret_key = os.getenv('SECRET_KEY')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

from app.extensions import db

from app.models import User
from app.models import Content

with app.app_context():
    db.create_all()

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    # Here you would write the logic to get the user from the database
    # For example, User.query.get(user_id)
    return User.query.get(user_id)

from app import routes
from app import admin_routes