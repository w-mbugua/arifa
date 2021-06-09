from django.db import models
from django.contrib.auth.models import AbstractUser
from markets.models import Market


class CustomUser(AbstractUser):
    occupation = models.CharField(max_length=50, null=True, blank=True)
    is_investor = models.BooleanField(default=False)
    is_expert = models.BooleanField(default=False)
   

    def get_field(self):
        return self.expertise


class Investor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    interests = models.ManyToManyField(Market, related_name='interested_investors')
    


    


