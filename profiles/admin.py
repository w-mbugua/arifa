from django.contrib import admin
from .models import Profile, Client, Message


admin.site.register(Profile)
admin.site.register(Client)
admin.site.register(Message)