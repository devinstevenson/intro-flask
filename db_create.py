from project import db
from project.models import BlogPost


db.create_all()
db.session.add(BlogPost("Good", "I\'m good."))
db.session.add(BlogPost("Well", "I\'m well."))
db.session.add(BlogPost("Excellent", "I\'m excellent."))
db.session.add(BlogPost("Okay", "I\'m okay."))
db.session.add(BlogPost("postgres", "we setup a local postgres instance"))

db.session.commit()
