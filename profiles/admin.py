from django.contrib import admin
from .models import Profile, Client, Message, Contact, Review


admin.site.register(Profile)
admin.site.register(Client)
admin.site.register(Message)
admin.site.register(Contact)
admin.site.register(Review)