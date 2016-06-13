import os
from functools import wraps
from flask import (Flask, session, render_template,
                   redirect, url_for, request, flash)
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(os.getenv('APP_SETTINGS'))
db = SQLAlchemy(app)
from models import *
from project.users.views import users_blueprint, login_required

app.register_blueprint(users_blueprint)

@app.route('/')
@login_required
def home():
    posts = db.session.query(BlogPost).all()
    return render_template('index.html', posts=posts)

@app.route('/welcome')
def welcome():
    return render_template("welcome.html")


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
