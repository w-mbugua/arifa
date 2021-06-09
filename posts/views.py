from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostCreateForm
from django.http import JsonResponse

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


@login_required
def create_post(request):
    form = PostCreateForm()
    if request.method == 'POST':
        form = PostCreateForm(request.POST)
        if form.is_valid():
                author = request.user
                post = form.save(commit=False)
                post.author = author
                post.save()
                
                # data = []
                # item = {"id": post.id, "body": post.body, "author": post.author.username,}
                # data.append(item)
                return redirect('home')
    return render(request, 'posts/addpost.html', {"form": form})
