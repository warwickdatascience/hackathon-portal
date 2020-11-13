from flask import Blueprint, request, render_template, jsonify, redirect, make_response, url_for
from flask import current_app as app
from flask_login import login_user
from .models import User 
from . import jwt
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_refresh_token_required, set_access_cookies, set_refresh_cookies, get_jwt_identity
import hashlib

# blueprint configuration
auth_bp = Blueprint("auth_bp", __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        # get username and password from database
        user = User.query.filter_by(username=request.form['username']).first()
        if user is None:
            error = f'Invalid Credentials. Please try again.'
        else:
            username = user.username
            password = user.password
            salt = user.salt
            # hash user password
            entered_pass = request.form["password"]
            key = hashlib.pbkdf2_hmac(
                'sha256', # The hash digest algorithm for HMAC
                entered_pass.encode('utf-8'), # Convert the password to bytes
                salt, # Provide the salt
                100000 # It is recommended to use at least 100,000 iterations of SHA-256 
            )
        
            # compare the values
            if request.form['username'] != username or key != password:
                error = f'Invalid Credentials. Please try again.'
            else:
                login_user(user, remember=True)
                return redirect(url_for('submission_bp.index'))
    return render_template('login.html', error=error)

