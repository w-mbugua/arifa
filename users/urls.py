from django.urls import path
from .views import home, SignUpView, landing_page, InvestorSignUpView, ExpertSignUpView 
from django.contrib.auth.views import LoginView
from profiles.views import create_profile
from profiles.views import client_messages

urlpatterns = [
    path('', landing_page, name="landing_page"),
    path('register/', SignUpView.as_view(), name='signup'),
    path('register/investor/', InvestorSignUpView.as_view(), name='investor_signup'),
    path('register/expert/', ExpertSignUpView.as_view(), name='expert_signup'),
    path('home/feed/', home, name='home'),
    path('newprofile/', create_profile, name='create_profile'),
    path('create_profile/', create_profile, name='create_profile'),
    path('my_quries/', client_messages, name="my_messages"),
]