from django.urls import path
from .views import home, SignUpView
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', SignUpView.as_view(), name='signup'),
    path('home/feed/', home, name='home'),
]