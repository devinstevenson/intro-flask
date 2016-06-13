import os
from functools import wraps
from flask import (Flask, session, render_template, Blueprint,
                   redirect, url_for, request, flash)
from app import app
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

##############
# # CONFIG # #
##############

users_blueprint = Blueprint('users', __name__, template_folder='templates')

###############
# # HELPERS # #
###############

# login decorator
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('users.login'))
    return wrap


##############
# # ROUTES # #
##############


@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        user = request.form.get('username')
        pw = request.form.get('password')
        if user != 'admin' or pw != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@users_blueprint.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('welcome'))
