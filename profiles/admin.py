from django.contrib import admin
from .models import Profile, Client, Message, Review, Reply


admin.site.register(Profile)
admin.site.register(Client)
admin.site.register(Message)
admin.site.register(Review)
admin.site.register(Reply)