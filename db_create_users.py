from project import db
from project.models import User


db.session.add(User("devin", "emberdesign@gmail.com", "secretkey2"))
db.session.add(User("admin", "admin@admin.com", "admin"))

db.session.commit()
