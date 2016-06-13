# from functools import wraps
from flask import (Blueprint, render_template)
from flask_login import login_required
from project import db
from project.models import BlogPost

##############
# # CONFIG # #
##############

home_blueprint = Blueprint('home', __name__, template_folder='templates')

###############
# # HELPERS # #
###############

# # login decorator
# def login_required(f):
#     @wraps(f)
#     def wrap(*args, **kwargs):
#         if 'logged_in' in session:
#             return f(*args, **kwargs)
#         else:
#             flash('You need to login first.')
#             return redirect(url_for('users.login'))
#     return wrap


@home_blueprint.route('/')
@login_required
def home():
    posts = db.session.query(BlogPost).all()
    return render_template('index.html', posts=posts)


@home_blueprint.route('/welcome')
def welcome():
    return render_template("welcome.html")
