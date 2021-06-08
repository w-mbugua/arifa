from django.shortcuts import render, redirect
from django.views.generic import CreateView, View
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from django.http import JsonResponse

from .email import send_welcome_email

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse

from posts.forms import PostCreateForm
from posts.models import Post


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup/registration_form.html'

    def form_valid(self, form):
        name = form.cleaned_data['username']
        email = form.cleaned_data['email']
        # send_welcome_email(name, email)
        return super().form_valid(form)


def home(request):
    form = PostCreateForm()
    user = request.user 
    posts = Post.objects.all().order_by('-pk')
       
    context = {"form": form, "posts": posts}
    return render(request, 'home.html', context)








