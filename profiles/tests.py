from django.test import TestCase
from .models import Profile, Message, Reply, Review, Client
from django.contrib.auth import get_user_model



class ProfileModelTest(TestCase):
    def setUp(self):
        self.user1 =  get_user_model().objects.create_user(username = 'testuser', email = 'test@email.com', password='secret')

        self.new_profile = Profile(user = self.user1, bio='here to test')
    
    def test_profile_instance(self):
        self.assertTrue(isinstance(self.new_profile, Profile))
    
    def test_string_method(self):
        self.assertEqual(str(self.new_profile), self.user1.username)

class MessageModelTest(TestCase):
    def setUp(self):
        self.user1 =  get_user_model().objects.create_user(username = 'testuser', email = 'test@email.com', password='secret')
        self.new_profile = Profile(user = self.user1, bio='here to test')
        self.new_msg = Message(to=self.new_profile, f_rom=self.user1, subject='Nothing', message="get back to me asap")
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_msg, Message))

