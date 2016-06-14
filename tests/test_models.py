import unittest
from flask_login import current_user
from base import BaseTestCase
from project import bcrypt
from project.models import User


class TestUser(BaseTestCase):
    # Ensure user can register
    def test_user_registration(self):
        with self.client:
            response = self.client.post('/register',
                                        data=dict(username="admin",
                                                  email="ad@min.com",
                                                  password="adminadmin",
                                                  confirm="adminadmin"),
                                        follow_redirects=True)
            self.assertIn(b'Welcome to Flask!', response.data)
            self.assertTrue(current_user.name == "admin")
            self.assertTrue(current_user.is_active())
            user = User.query.filter_by(email='ad@min.com').first()
            self.assertTrue(str(user) == '<name - admin>')

    def test_get_by_id(self):
        # Ensure id is correct for the current/logged in user
        with self.client:
            self.client.post('/login',
                             data=dict(username="admin", password='adminadmin'),
                             follow_redirects=True)
            self.assertTrue(current_user.id == 1)
            self.assertFalse(current_user.id == 20)

    def test_check_password(self):
        # Ensure given password is correct after unhashing
        user = User.query.filter_by(email='ad@min.com').first()
        self.assertTrue(bcrypt.check_password_hash(user.password, 'adminadmin'))
        self.assertFalse(bcrypt.check_password_hash(user.password, 'foobar'))


if __name__ == '__main__':
    unittest.main()
