from functools import wraps
from flask import (Blueprint, session, render_template,
                   redirect, url_for, request, flash)
from forms import LoginForm
from project.models import User, bcrypt


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
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            pw = request.form.get('password')
            user = User.query.filter_by(name=request.form['username']).first()
            if user is not None and bcrypt.check_password_hash(user.password, pw):
                session['logged_in'] = True
                flash('You were logged in')
                return redirect(url_for('home.home'))
            else:
                error = 'Invalid Credentials. Please try again.'
    return render_template('login.html', form=form, error=error)

@users_blueprint.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('home.welcome'))
