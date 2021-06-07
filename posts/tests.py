from django.test import TestCase
from .models import Post
from django.contrib.auth import get_user_model


class PostModelTest(TestCase):
    def setUp(self):
        self.user1 =  get_user_model().objects.create_user(
            username = 'testuser',
            email = 'test@email.com',
            password='secret'
        )

        self.new_post = Post(author=self.user1, body='evening! this is a tesing post')
    
    def test_post_instance(self):
        self.assertTrue(isinstance(self.new_post, Post))
    
    def test_to_string_method(self):
        self.assertEqual(str(self.new_post), 'evening! this is a t')
       
