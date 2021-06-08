from django import forms
from .models import Profile, Message

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        exclude = ('to', 'f_rom')

class ReplyForm(forms.Form):
    response = forms.CharField(widget=forms.Textarea())
