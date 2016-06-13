from app import db
from models import BlogPost


db.create_all()
db.session.add(BlogPost("Good", "I\'m good"))
db.session.add(BlogPost("Well", "I\'m well"))

db.session.commit()
