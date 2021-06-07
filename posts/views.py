from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'posts/post_delete.html'
    success_url = reverse_lazy('home')

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'posts/update.html'
    fields = ('body', 'image',)

class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
