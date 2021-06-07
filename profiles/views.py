from django.shortcuts import render
from django.views.generic import DetailView, UpdateView, ListView, CreateView
from .models import Profile
from .forms import UserProfileForm
from django.contrib.auth.mixins import LoginRequiredMixin

class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'profiles/profile_detail.html'

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = ('bio', 'photo', 'neighborhood',)
    template_name = 'profiles/profile_edit.html'

class ProfileListView(LoginRequiredMixin, ListView):
    model = Profile
    context_object_name = 'profiles_list'
    template_name = 'profiles/profiles_list.html'

class ProfileCreateView(LoginRequiredMixin, CreateView):
    form_class = UserProfileForm
    model = Profile
    template_name = 'profiles/profile_reg.html'

    def form_valid(self, form):
        profile = form.save(commit=False)
        profile.user = self.request.user
        profile.save()
        return super().form_valid(form)
