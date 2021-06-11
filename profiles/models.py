from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from cloudinary.models import CloudinaryField
from posts.models import Post
from django.template.defaultfilters import slugify
from markets.models import Market
from users.models import CustomUser


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField()
    photo = CloudinaryField('image')
    created = models.DateTimeField(auto_now_add=True)
    experience = models.IntegerField()
    employer = models.CharField(max_length=50, null=True, blank=True)
    slug = models.SlugField(unique=True)
    market = models.ForeignKey(Market, on_delete=models.CASCADE, related_name='experts')
    followers = models.ManyToManyField(get_user_model(), related_name='followers')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user)
        super(Profile, self).save(*args, **kwargs)


    def __str__(self):
        return self.user.username
    
    def get_absolute_url(self):
        return reverse('profile', args=[str(self.slug)])
    
    def get_posts(self):
        posts = Post.objects.filter(author=self.user)
        return posts 
    
    def get_messages(self):
        return self.messages.all()
    
    def get_clients(self):
        clients = self.clients.all()
        names = []
        for client in clients:
            names.append(client.name)
        return names
    
    @classmethod
    def search_profile(cls, p_name):
        profile = cls.objects.filter(user__username__icontains = p_name)
        return profile


class Client(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    client_of = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='clients') # expert
    
    def __str__(self):
        return f"{self.name} client of {self.client_of}"


class Message(models.Model):
    to = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='messages')
    subject = models.CharField(max_length=200)
    message = models.TextField()
    f_rom = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='queries')
    sent = models.DateTimeField(auto_now_add=True)
    response = models.TextField()

    def __str__(self):
        return f"to {self.to} from {self.f_rom}"

class Reply(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='replies')
    response = models.TextField()
    sender = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

class Review(models.Model):
    body = models.CharField(max_length=500)
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    reviewed = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='reviews')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body[:50]
    
    class Meta:
        ordering = ('-created',)
    




