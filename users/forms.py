from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import widgets
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('email', 'occupation',)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields

class NewsLetterForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField()



