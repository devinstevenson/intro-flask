import os
from flask import (Flask)
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config.from_object(os.getenv('APP_SETTINGS'))
db = SQLAlchemy(app)

from project.users.views import users_blueprint
from project.home.views import home_blueprint

app.register_blueprint(users_blueprint)
app.register_blueprint(home_blueprint)
