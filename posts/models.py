from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericRelation
from comment.models import Comment


class Post(models.Model):
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE, related_name='posts')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    comments = GenericRelation(Comment)
    likes = models.ManyToManyField(get_user_model(), related_name='posts_liked', blank=True)


    def __str__(self):
        return self.body[:20]
    
    def get_absolute_url(self):
         return reverse('post_detail', args=[str(self.id)])

    def get_likes(self):
        return self.likes.all().count()

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    body = models.TextField()
    link = models.URLField()
    image_url = models.URLField()
    pub_time = models.DateTimeField()

    def __str__(self):
        return self.title