from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import widgets
from posts.models import Post

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('author', 'likes')
        widgets = {
            'body': forms.Textarea(attrs={'rows': '3'})
        }



