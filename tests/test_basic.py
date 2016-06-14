import unittest  # pragma: no cover
from base import BaseTestCase  # pragma: no cover


class FlaskTestCase(BaseTestCase):
    def test_index(self):
        response = self.client.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensure that main page requires user login
    def test_main_route_requires_login(self):
        response = self.client.get('/', follow_redirects=True)
        self.assertIn(b'Please log in to access this page.', response.data)

    # Ensure that logout page requires user login
    def test_logout_route_requires_login(self):
        response = self.client.get('/logout', follow_redirects=True)
        self.assertIn(b'Please log in to access this page.', response.data)

    # Ensure that posts show up on the main page
    def test_posts_show_up_on_main_page(self):

        response = self.client.post('/login',
                                    data=dict(username="admin", password="adminadmin"),
                                    follow_redirects=True)
        self.assertIn(b'This is a test. Only a test.', response.data)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()  # pragma: no cover
