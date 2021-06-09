from django.urls import path
from .views import home, SignUpView, landing_page
from django.contrib.auth.views import LoginView
from profiles.views import create_profile

urlpatterns = [
    path('', landing_page, name="landing_page"),
    path('register/', SignUpView.as_view(), name='signup'),
    path('home/feed/', home, name='home'),
    path('newprofile/', create_profile, name='create_profile'),
    path('create_profile/', create_profile, name='create_profile'),
]