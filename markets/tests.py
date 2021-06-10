from django.test import TestCase
from .models import Market

# Create your tests here.
class MarketModelTests(TestCase):
    def setUp(self):
        self.new_market = Market(name='stocks', slug='stocks')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_market, Market)) 
