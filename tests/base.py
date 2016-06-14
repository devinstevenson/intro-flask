from flask_testing import TestCase  # pragma: no cover
from project import app, db  # pragma: no cover
from project.models import User, BlogPost  # pragma: no cover

class BaseTestCase(TestCase):
    def create_app(self):
        app.config.from_object('config.TestConfig')
        return app

    # must use these function names
    def setUp(self):
        db.create_all()
        db.session.add(BlogPost("Test post", "This is a test. Only a test.", 1))
        db.session.add(User("admin", "ad@min.com", "adminadmin"))
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
