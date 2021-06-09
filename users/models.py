from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    occupation = models.CharField(max_length=50, null=True, blank=True)
   

    def get_field(self):
        return self.expertise


    


