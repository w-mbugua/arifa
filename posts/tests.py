from django.contrib import auth
from django.test import TestCase
from .models import Post, BlogPost
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

class BlogPostModelTest(TestCase):
    def setUp(self):
        self.news_post = BlogPost(title="news alert!", author="jane doe", body="how to invest in the stocks market", link="https://newstar.com", image_url="https://image.com")
    
    def test_instance(self):
        self.assertTrue(isinstance(self.news_post, BlogPost))
    
    def test_string_method(self):
        self.assertTrue(str(self.news_post), self.news_post.title)
       
