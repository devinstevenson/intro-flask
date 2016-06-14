from base import BaseTestCase  # pragma: no cover


class BlogPostsTests(BaseTestCase):
    def test_user_can_post(self):
        with self.client:
            self.client.post('/login',
                             data=dict(username="admin", password="adminadmin"),
                             follow_redirects=True)
            response = self.client.post('/',
                                        data=dict(title="test", description="test"),
                                        follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'New entry was successfully posted. Thanks.', response.data)
