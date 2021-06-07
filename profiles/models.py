from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from cloudinary.models import CloudinaryField


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField()
    photo = CloudinaryField('image')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    
    def get_absolute_url(self):
        return reverse('profile', args=[str(self.pk)])
