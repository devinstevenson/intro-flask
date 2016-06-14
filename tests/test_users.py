import unittest  # pragma: no cover
from flask import request  # pragma: no cover
from flask_login import current_user  # pragma: no cover
from base import BaseTestCase  # pragma: no cover
from project import bcrypt  # pragma: no cover
from project.models import User  # pragma: no cover


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

    def test_incorrect_user_registeration(self):
        with self.client:
            response = self.client.post('/register', data=dict(
                username='Michael', email='michael',
                password='python', confirm='python'
            ), follow_redirects=True)
            self.assertIn(b'Invalid email address.', response.data)
            self.assertIn(b'/register', request.url)

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


class UsersViewsTests(BaseTestCase):
    # Ensure that the login page loads correctly
    def test_login_page_loads(self):
        response = self.client.get('/login')
        self.assertIn(b'Please login', response.data)

    # Ensure login behaves correctly with correct credentials
    def test_correct_login(self):
        with self.client:
            response = self.client.post('/login',
                                        data=dict(username="admin",
                                                  password="adminadmin"),
                                        follow_redirects=True)
            self.assertIn(b'You were logged in', response.data)
            self.assertTrue(current_user.name == "admin")
            self.assertTrue(current_user.is_active())

    # Ensure login behaves correctly with incorrect credentials
    def test_incorrect_login(self):
        response = self.client.post('/login',
                                    data=dict(username="wrong", password="wrong"),
                                    follow_redirects=True)
        self.assertIn(b'Invalid Credentials. Please try again.', response.data)

    # Ensure logout behaves correctly
    def test_logout(self):
        with self.client:
            self.client.post('/login',
                             data=dict(username="admin", password="adminadmin"),
                             follow_redirects=True)
            response = self.client.get('/logout', follow_redirects=True)
            self.assertIn(b'You were logged out', response.data)
            self.assertFalse(current_user.is_active())

    def test_logout_route_requires_login(self):
        response = self.client.get('/logout', follow_redirects=True)
        self.assertIn(b'Please log in to access this page', response.data)

if __name__ == '__main__':
    unittest.main()
