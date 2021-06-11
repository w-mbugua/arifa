from django.shortcuts import render, redirect
from django.views.generic import CreateView, View
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, ExpertSignUpForm, NewsLetterForm, InvestorSignUpForm
from .models import CustomUser
from django.http import JsonResponse
from django.contrib.auth import login

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse

from posts.forms import PostCreateForm
from posts.models import Post
from profiles.models import Profile



class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('create_profile')
    template_name = 'signup/signup.html'

    def form_valid(self, form):
        name = form.cleaned_data['username']
        email = form.cleaned_data['email']
        # send_welcome_email(name, email)
        return super().form_valid(form)

class InvestorSignUpView(CreateView):
    model = CustomUser
    form_class = InvestorSignUpForm
    template_name = 'signup/registration_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'investor'
        return super().get_context_data(**kwargs)
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class ExpertSignUpView(CreateView):
    model = CustomUser
    form_class = ExpertSignUpForm
    template_name = 'signup/registration_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'expert'
        return super().get_context_data(**kwargs)
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('create_profile')

@login_required
def home(request):
    form = PostCreateForm()
    user = request.user 
    profiles = Profile.objects.all()
    p = ''
    val = False
    if user.is_expert:
        for profile in profiles:
            if profile.user == user:
                val = True
                p = profile
    print(val)
    print(p)
    posts = Post.objects.all().order_by('-pk')

    context = {"form": form, "posts": posts, "profiles": profiles, "val": val, "p": p}
    return render(request, 'home.html', context)

def landing_page(request):
    form = NewsLetterForm()
    return render(request, 'landing.html', {"form": form})






