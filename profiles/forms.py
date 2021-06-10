from django import forms
from django.forms import widgets
from .models import Profile, Message, Review, Reply

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('expertise', 'user', 'slug', 'following',)
        widgets = {
            'bio': forms.Textarea(attrs={'rows': '3'})
        }

class Registration2Form(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('following', )
        fields = ('expertise', 'experience', 'employer',)

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        exclude = ('to', 'f_rom', 'response',)

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ('response',)
        widgets = {
            'response': forms.Textarea(attrs={'rows': '2'})
        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ('user', 'reviewed',)
        widgets = {
            'body': forms.Textarea(attrs={'rows': '3'})
        }