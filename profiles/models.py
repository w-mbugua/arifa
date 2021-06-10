from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from cloudinary.models import CloudinaryField
from posts.models import Post
from django.template.defaultfilters import slugify
from markets.models import Market

EXPERTISE_CHOICES = (('Equities', 'Equities'), ('Money Market', 'Money Market'), ('Real Estate', 'Real Estate'), ('Crypto', 'Crypto'))
class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField()
    photo = CloudinaryField('image')
    created = models.DateTimeField(auto_now_add=True)
    expertise = models.CharField(choices=EXPERTISE_CHOICES, max_length=12)
    experience = models.IntegerField()
    employer = models.CharField(max_length=50, null=True, blank=True)
    slug = models.SlugField(unique=True)
    market = models.ForeignKey(Market, on_delete=models.CASCADE, related_name='experts')
    following = models.ManyToManyField('self', through='Contact', related_name='followers', symmetrical=False)

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




class Contact(models.Model):
        user_from = models.ForeignKey(Profile, related_name='rel_from_set', on_delete=models.CASCADE)
        user_to = models.ForeignKey(Profile, related_name='rel_to_set', on_delete=models.CASCADE)
        created = models.DateTimeField(auto_now_add=True)
        
        class Meta:
            ordering = ('-created',)
        def __str__(self):
            return f'{self.user_from} follows {self.user_to}'

class Client(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    client_of = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='clients')
    
    def __str__(self):
        return f"{self.name} client of {self.client_of}"


class Message(models.Model):
    to = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='messages')
    subject = models.CharField(max_length=200)
    message = models.TextField()
    f_rom = models.ForeignKey(Client, on_delete=models.CASCADE)
    sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"to {self.to} from {self.f_rom.name}"

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
    




