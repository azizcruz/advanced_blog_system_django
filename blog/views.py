from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.

# HOMEPAGE VIEW.
def home(request):
    context = {
        'posts': Post.objects.all(),
        'title': 'Home'
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_created']
    paginate_by = 3

    extra_context = {
        'title': 'Home'
    }

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/users_posts.html'
    paginate_by = 5
    context_object_name = 'posts'

    extra_context = {
        'title': 'User Posts'
    }

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_created')


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    print(model)
    extra_context = {
    'title': 'post'
    }

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/new_post.html'
    fields = ['title', 'content']
    extra_context = {
        'title': 'new'
    }

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    extra_context = {
        'title': 'Update'
    }
    template_name = 'blog/new_post.html'
    fields = ['title', 'content']

    def test_func(self):
        post = self.get_object()

        # Check if the current user is the post writer.
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/are_you_sure.html'
    success_url = '/'

    def test_func(self):
        post = self.get_object()

        if self.request.user == post.author:
            return True
        return False