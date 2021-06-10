from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import widgets
from django.db import transaction
from .models import CustomUser, Investor
from markets.models import Market


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields

class NewsLetterForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField()

class InvestorSignUpForm(UserCreationForm):
    interests = forms.ModelMultipleChoiceField(
        queryset=Market.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('email',)

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_investor = True
        user.save()
        investor = Investor.objects.create(user=user)
        investor.interests.add(*self.cleaned_data.get('interests'))
        return user

class ExpertSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_expert = True
        if commit:
            user.save()
        return user



